import raga
import util
import json
import pickle

raag_file = "/Users/simjega/source/raags/process_output_tmp.json"
raag_file_json = json.load(open(raag_file, "r"))

known_raags = []
failed_raags = 0

aroha_fail_count = 0
avroha_fail_count = 0
both_fail_count = 0

def print_problems(note_strings, sign):
    a = None
    problems = []
    for i in range(len(note_strings)):
        if i is 0:
            continue

        diff = util.convert_name_to_metric(note_strings[i]) - util.convert_name_to_metric(note_strings[i - 1])

        if (diff > 0) is not (sign > 0):
            problems.append(note_strings[i - 1 : i + 1])

    return ", ".join(["{0} -> {1}".format(*map(str, problem)) for problem in problems])


for raag_name, raag_repr in raag_file_json.iteritems():
    # print "processing {0}".format(raag_name)

    ascending = raag_repr["ascending-scale"]
    descending = raag_repr["descending-scale"]

    aroha = None
    try:
        aroha = util.aroha(map(util.convert_name_to_note, ascending))

    except AssertionError:
        aroha_fail_count += 1
        print "ordering failed for aroha of {0}: {1}".format(raag_name, print_problems(ascending, 1))

    avroha = None
    try:
        avroha = util.avroha(map(util.convert_name_to_note, descending))

    except AssertionError:
        avroha_fail_count += 1
        print "ordering failed for avroha of {0}: {1}".format(raag_name, print_problems(descending, -1))

    if aroha is None and avroha is None:
        both_fail_count += 1

    if aroha is not None and avroha is not None:
        # print "succeeded"
        pass
        r = raga.Raga(aroha, avroha)
        print "{}: \n{}".format(raag_name, r)
        known_raags.append(r)
    else:
        # print "failed"
        failed_raags += 1

print
print "processed: {0}, failed: {1}".format(len(known_raags), failed_raags)
print "failure reasons: aroha order: {0}, avroha order: {1}, both order: {2}".format(aroha_fail_count,
                                                                                     avroha_fail_count, both_fail_count)

pickle.dump(known_raags, open("known_raags.pkl", "w"))
