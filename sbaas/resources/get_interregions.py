#!/usr/bin/env python
import sys
import Bio
from Bio import SeqIO, SeqFeature
from Bio.SeqRecord import SeqRecord
import os
 
# Copyright(C) 2009 Iddo Friedberg & Ian MC Fleming
# Released under Biopython license. http://www.biopython.org/DIST/LICENSE
# Do not remove this comment
def get_interregions(genbank_path,intergene_length=1):
    seq_record = SeqIO.parse(open(genbank_path), "genbank").next()
    cds_list_plus = []
    cds_list_minus = []
    intergenic_records = []
    intergenic_features = []
    # Loop over the genome file, get the CDS features on each of the strands
    for feature in seq_record.features:
        if feature.type == 'CDS':
            mystart = feature.location.start.position
            myend = feature.location.end.position
            if feature.strand == -1:
                cds_list_minus.append((mystart,myend,-1))
            elif feature.strand == 1:
                cds_list_plus.append((mystart,myend,1))
            else:
                sys.stderr.write("No strand indicated %d-%d. Assuming +\n" %
                                  (mystart, myend))
                cds_list_plus.append((mystart,myend,1))
 
    for i,pospair in enumerate(cds_list_plus[1:]):
        # Compare current start position to previous end position
        last_end = cds_list_plus[i][1]
        this_start = pospair[0]
        strand = pospair[2]
        if this_start - last_end >= intergene_length:
            intergene_seq = seq_record.seq[last_end:this_start]
            featurelocation = SeqFeature.FeatureLocation(last_end,this_start,strand=+1);
            strand_string = "+"
            sequencerecord = SeqRecord(intergene_seq,id="%s-ign-%d" % (seq_record.name,i),
                  description="%s %d-%d %s" % (seq_record.name, last_end+1,
                                                        this_start,strand_string))
            sequencerecord.features = [featurelocation];
            intergenic_features.append(featurelocation);
            intergenic_records.append(sequencerecord);
            #intergenic_records.append(
            #      SeqRecord(intergene_seq,id="%s-ign-%d" % (seq_record.name,i),
            #      description="%s %d-%d %s" % (seq_record.name, last_end+1,
            #                                            this_start,strand_string)))
    for i,pospair in enumerate(cds_list_minus[1:]):
        last_end = cds_list_minus[i][1]
        this_start = pospair[0]
        strand = pospair[2]
        if this_start - last_end >= intergene_length:
            intergene_seq = seq_record.seq[last_end:this_start]
            featurelocation = SeqFeature.FeatureLocation(last_end,this_start,strand=-1);
            strand_string = "-"
            sequencerecord = SeqRecord(intergene_seq,id="%s-ign-%d" % (seq_record.name,i),
                  description="%s %d-%d %s" % (seq_record.name, last_end+1,
                                                        this_start,strand_string))
            sequencerecord.features = [featurelocation];
            intergenic_features.append(featurelocation);
            intergenic_records.append(sequencerecord);
            #intergenic_records.append(
            #      SeqRecord(intergene_seq,id="%s-ign-%d" % (seq_record.name,i),
            #      description="%s %d-%d %s" % (seq_record.name, last_end+1,
            #                                            this_start,strand_string)))
    #outpath = os.path.splitext(os.path.basename(genbank_path))[0] + "_ign.fasta"
    #SeqIO.write(intergenic_records, open(outpath,"w"), "fasta")
    return intergenic_features;
 
if __name__ == '__main__':
    if len(sys.argv) == 2:
         get_interregions(sys.argv[1])
    elif len(sys.argv) == 3:
         get_interregions(sys.argv[1],int(sys.argv[2]))
    else:
         print "Usage: get_intergenic.py gb_file [intergenic_length]"
         sys.exit(0)