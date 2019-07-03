from bioUtilities.files import MODULE_DIR, fasta_from_bed, remove_file, read_fasta
import unittest
import os

class TestFastaFromBed(unittest.TestCase):

    def test_fasta_from_bed1(self):
        input_bed = "{0}/tests/data/input.bed".format(MODULE_DIR)
        input_genome_fasta = "{0}/tests/data/test_genome.fa".format(MODULE_DIR)
        input_genome_fasta_index = "{0}/tests/data/test_genome.fa.fai".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_fasta_from_bed1.fa".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_fasta_from_bed1.fa".format(MODULE_DIR)
        remove_file(observed_file)
        remove_file(input_genome_fasta_index)
        fasta_from_bed(input_bed, input_genome_fasta, observed_file)
        observed = read_fasta(observed_file)
        expected = read_fasta(expected_file)
        self.assertEqual(observed, expected)
        remove_file(observed_file)

    def test_fasta_from_bed2(self):
        input_bed = "{0}/tests/data/input.bed".format(MODULE_DIR)
        input_genome_fasta = "{0}/tests/data/test_genome.fa".format(MODULE_DIR)
        input_genome_fasta_index = "{0}/tests/data/test_genome.fa.fai".format(MODULE_DIR)
        expected_file = "{0}/tests/data/expected_fasta_from_bed2.fa".format(MODULE_DIR)
        observed_file = "{0}/tests/data/observed_fasta_from_bed2.fa".format(MODULE_DIR)
        remove_file(observed_file)
        remove_file(input_genome_fasta_index)
        fasta_from_bed(input_bed, input_genome_fasta, observed_file, names = True)
        observed = read_fasta(observed_file)
        expected = read_fasta(expected_file)
        self.assertEqual(observed, expected)
        remove_file(observed_file)
