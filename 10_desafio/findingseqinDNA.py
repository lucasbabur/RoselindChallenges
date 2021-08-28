def FindInSEQ(seq, string):

    jumper = seq.split(string)
    total_len = 0
    index_array = []

    for ocurrences in jumper:
        index_array.append(len(ocurrences) + 1 + total_len)
        total_len = len(ocurrences) + 1 + total_len
    index_array.pop(len(index_array) - 1)
    return index_array


print(FindInSEQ("CCGGAGAGAAGAGAGAAGAGAGAGAAGAGAGAGAACGTGAGAGAACGATGGAGAGAACCCGAGAGAAAGAGAGAAGGGAGAGAAGGGGAGAGAACAGGGGAGAGAATCGAGAGAGAATGAGAGAATAGAGAGAAAGAGAGAAGAGAGAACGAGAGAAACATCCAACTGGCGGAGAGAATCACCCGTGAGAGAATCGGGAGAGAAGTGTCGAGAGAACGTGAGAGAAACATGAGAGAAAGAGAGAATAGGAGAGAACGAGAGAAGAGAGAACGTGAGAGAACCGAGAGAAAGAGAGAAGAGAGAACCGAGAGAATCAGAGAGAAGAGAGAAACAGAGAGAGAAGGCGGGAGAGAATATAGAGAGAACGGGGAGAGAACAGAGAGAACGCGTGCGATGAGAGAAGCAAGAGAGAAGAGAGAAAGAGAGAAGAGAGAATTACACGCGAGAGAATGGAGAGAAGAGAGAAAATGAGAGAAGAGAGAATGAGAGAAGAGAGAATACCCTGAGCGAGAGAAGAGAGAAAAGGAGAGAGAAACTGTCAGAGAGAAACGAGAGAAGAGAGAATAGAGAGAAGAGAGAACCACGAGAGAACCGAGAGAAGGCGAGAGAGAACTTATAAGTGAGAGAAAGCGAGAGAAAGGAGAGAATATACGGAGAGAAGGAGAGAATCGGAGAGAAGAGAGAAGAGAGAAGGAGAGAGAAGAGAGAAGAGAGAATTTGAGAGAACTGAGAGAAGAGAGAAAGAGAGAAACGGAGAGAAGAGAGAAATAAGATCGCACAATGAGAGAAATTATCATGCCGAGAGAAAACAACGAGAGAAAGAGAGAAGCATTTCGCTGAAAGTTGAGAGAAAGCTACAGAGAGAATTATCCCCGAGAGAACCGAGAGAAACAAGAGAGAACTGAGAGAACTGAGAGAACCCGAGAGAA", "GAGAGAAGA"))