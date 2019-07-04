import collections

from bioUtilities.files import read_many_fields

def get_exon_junctions(input_bed, output_file, all_exons_file = None):
    """
    Given a .bed file, return all the exon junctions

    Parameters
    ---------
    input_bed : str
        Path to the input bed file
    output_file : str
        Path to the output file
    all_exons_file : str
        If set, path to a file containing all exons to get junctions that might
        not appear in the main set because you may have just coding exons

    Examples
    ---------
    >>> from bioUtilities.splice import get_exon_junctions
    >>> get_exon_junctions("coding_exons.bed", "exon_junctions.bed", all_exons_file = "all_exons.bed")
    """


    entries = read_many_fields(input_bed)

    # index each of the entries
    entry_exons = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict())))
    for entry in entries:
        entry_exons[entry[0]][entry[5]][entry[3].split(".")[0]][int(entry[3].split(".")[1])] = [int(entry[1]), int(entry[2])]

    # if the file containing all exons has been given too
    if all_exons_file:
        all_entries = read_many_fields(all_exons_file)
        all_exons = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict())))
        for entry in all_entries:
            all_exons[entry[0]][entry[5]][entry[3].split(".")[0]][int(entry[3].split(".")[1])] = [int(entry[1]), int(entry[2])]

    retained = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict()))

    for chr in entry_exons:
        for strand in entry_exons[chr]:
            for transcript_id in entry_exons[chr][strand]:
                for exon_id in sorted(entry_exons[chr][strand][transcript_id]):
                    focal = entry_exons[chr][strand][transcript_id][exon_id]

                    # now get the each downstream case
                    try:
                        downstream = entry_exons[chr][strand][transcript_id][exon_id + 1]
                        if strand == "-":
                            junction = [downstream[1], focal[0]]
                        else:
                            junction = [focal[1], downstream[0]]
                        junction_id = "{0}-{1}".format(exon_id, exon_id + 1)
                        retained[chr][transcript_id][junction_id] = [junction, strand]
                    except:
                        try:
                            # these are cases where the downstream exon is a noncoding exon
                            # and the all exons has been defined
                            if all_exons_file:
                                downstream = all_exons[chr][strand][transcript_id][exon_id + 1]
                                if strand == "-":
                                    junction = [downstream[1], focal[0]]
                                else:
                                    junction = [focal[1], downstream[0]]
                                junction_id = "{0}-{1}".format(exon_id, exon_id + 1)
                                retained[chr][transcript_id][junction_id] = [junction, strand]
                        except:
                            pass

                    # upstream junction
                    upstream_junction_id = "{0}-{1}".format(exon_id - 1, exon_id)
                    if upstream_junction_id not in retained[chr][transcript_id]:
                        # get the case where the first coding exon has a noncoding exon upstream
                        try:
                            upstream = all_exons[chr][strand][transcript_id][exon_id - 1]
                            if strand == "-":
                                junction = [focal[1], upstream[0]]
                            else:
                                junction = [upstream[1], focal[0]]
                            retained[chr][transcript_id][upstream_junction_id] = [junction, strand]
                        except:
                            pass

    junctions = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict()))
    for chr in retained:
        for transcript_id in retained[chr]:
            for exon_junction in retained[chr][transcript_id]:
                exon1 = int(exon_junction.split("-")[0])
                exon2 = int(exon_junction.split("-")[1])
                info = retained[chr][transcript_id][exon_junction]
                junctions[chr][transcript_id][exon1] = [exon2] + info

    # now write each of the entries to the output file
    with open(output_file, "w") as outfile:
        for chr in sorted(junctions):
            for transcript_id in sorted(junctions[chr]):
                for exon1 in sorted(junctions[chr][transcript_id]):
                    info = junctions[chr][transcript_id][exon1]
                    exon2 = junctions[chr][transcript_id][exon1][0]
                    coordinates = junctions[chr][transcript_id][exon1][1]
                    strand = junctions[chr][transcript_id][exon1][2]
                    output = [chr, coordinates[0], coordinates[1], "{0}.{1}-{2}".format(transcript_id, exon1, exon2), ".",  strand]
                    outfile.write("{0}\n".format("\t".join([str(i) for i in output])))
