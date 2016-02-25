# -*- coding: utf-8 -*-
"""
Created on Thu Apr 02 22:01:14 2015

Please feel free to contact me for any question.
--
Zewei Song
University of Minnesota
Dept. Plant Pathology
songzewei@outlook.com
"""

#%%
def read_otu_map(filename):
    from lib import File_IO
    OtuMap = File_IO.read_file(filename)
    MapDict = {}
    for line in OtuMap:
        names = line.strip('\n').split('\t')
        MapDict[names[0]]=names[1:]
    return MapDict
#%%
class otu_map_parser(object):
    # Get basic information of an OTU map
    def __init__(self, Map):
        self.derep_count = len(Map)
        derep_size = [len(Map[i]) for i in Map]
        self.seqs_count = sum(derep_size)
        self.max_derep = max(derep_size)
        self.min_derep = min(derep_size)
        self.ave_derep = self.seqs_count/float(self.derep_count)


def get_rep_list(Map):
    rep_list = [i for i in Map]
    return rep_list

def filter_by_name(MapDict,otu_list,method='discard'):
# Pick or discard OTUs in the otu list from a Qiime OTU map.
    if method == 'discard':
        for otu in otu_list:
            del MapDict[otu]
        return MapDict
    elif method == 'keep':
        MapDict_keep = {}
        for otu in otu_list:
            MapDict_keep[otu] = MapDict[otu]
        return MapDict_keep
    else:
        print 'Wrong method: %s is not a valid method.'%method
        print 'use discard or keep'

def filter_by_size(MapDict,min_size=2):
#Filter OTU map by minimum size.
#By default it will remove all singletons.
    MapDict_Size = MapDict.copy()
    for item in MapDict:
        cluster_size = len(MapDict[item])
        if cluster_size < min_size:
            del MapDict_Size[item]
        else:
            pass
    return MapDict_Size


#%%
def write_otu_map(MapDict,output_file='new_map.txt'):
#Not sure for now if I should sort the otu names by number
#Probably not, it can be converted to otu table in Qiime.
    with open(output_file, 'wb') as f:
        for key, value in MapDict.items():
            cluster_seqs = '\t'.join(value)
            f.write('%s\t%s\n'%(key,cluster_seqs))


def extract_all_seqs(Map, otu_list):
# Extract all seqeunce names associated with the OTUs in the OTU list provided.
    import sys
    extracted = []
    for name in otu_list:
        try:
            for seq_name in Map[name]:
                extracted.append(seq_name)
        except ValueError:
            print 'Cannot find %s in the provided Qiime map.'
            sys.exit()
    return extracted


def generate_fast_style(input_otu_map, input_centroid, real_sample = False):
# Create a FAST style file that contains information of sequences and sample counts.
    fast_dict = {}
    centroid_dict = {}
    centroid_list = []
    
    # Remove USEARCH size label from sequence labels
    for record in input_centroid:
        current_label = record[0][:record[0].find(';')]
        centroid_dict[current_label] = record[1]
        centroid_list.append(current_label)
    
    new_otu_map = {}
    for key, value in input_otu_map:
        new_key = key[:key.find(';')]
        new_sample = []
        for item in value:
            if real_sample:
                new_sample.append(item[:item.find('_')]) # if it is real sample, get the sample name by locate the first "_"
            else:
                new_sample.append(item[:item.find(';')]) # if it is derep unit, get the derep name by locagte the first ";"
        
        new_otu_map[new_key] = new_sample
    
    for element in centroid_list:
        fast_dict[element] = {}
        fast_dict[element]['seq'] = centroid_dict[element]
        
        fast_dict[element]['sample'] = {}
        for sample in new_otu_map[element]:
            try:
                fast_dict[element]['sample'][sample] += 1
            except KeyError:
                fast_dict[element]['sample'][sample] = 1
    
    return fast_dict

"""
#%%Handling uc file from USEARCH
def read_uc_map(filename):
#Read in .uc file
    from lib import File_IO
    temp = File_IO.read_file(filename)
    UcMap = []
    for line in temp:
        if line[0] == "S" or line[0] == "H":
            temp_otu = line.strip('\n').split('\t')[-2:] #Get the last two column in each line
            UcMap.append(temp_otu)
    return UcMap


def convert_uc_map(UcMap):
    QiimeMap = {}
    for line in UcMap:
        if line[1] == "*": #this seq is a new cluster
            QiimeMap[line[0]]=[line[0]]
        else:
            QiimeMap[line[1]].append(line[0]) #this seq belongs to an existed cluster
    return QiimeMap
"""