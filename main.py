import raga
import util
import json
import pickle

# basic usage
# Raga Durga
# S R M P D S'
# S' D P M R S
# durga = raga.Raga(
#     util.aroha(map(util.convert_name_to_note, ["S", "R", "M", "P", "D", "S'"])),
#     util.avroha(map(util.convert_name_to_note, ["S'", "D", "P", "M", "R", "S"])))

raag_file = "/Users/simjega/source/raags/process_output_tmp.json"
raag_file_json = json.load(open(raag_file, "r"))

known_raags = []

for raag_name, raag_repr in raag_file_json.iteritems():
    print "processing {0}".format(raag_name)
    aroha = None
    try:
        aroha = util.aroha(map(util.convert_name_to_note, raag_repr["ascending-scale"]))

    except AssertionError:
        print "ordering failed for aroha of {}".format(raag_name)

    avroha = None
    try:
        avroha = util.avroha(map(util.convert_name_to_note, raag_repr["descending-scale"]))

    except AssertionError:
        print "ordering failed for avroha of {}".format(raag_name)

    if aroha is not None and avroha is not None:
        r = raga.Raga(aroha, avroha)
        print "{}: \n{}".format(raag_name, r)
        known_raags.append(r)

print len(known_raags)

pickle.dump(known_raags, open("known_raags.pkl", "w"))