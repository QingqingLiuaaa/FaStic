#!/usr/bin/env python3
import sys
import argparse

def fa_feature_statistic(args1):
    with open(args1) as fr:
        dict1 = {}
        A, T, C, G, N = 0, 0, 0, 0, 0
        count = 0
        Total = 0
        for line in fr:
            if line.startswith('>'):
                name = line.replace('>', '').strip().split()[0]
                dict1[name] = 0
                count += 1
            else:
                line = line.strip().upper()
                dict1[name] += len(line)
                Total += len(line)
                A += line.count('A')
                T += line.count('T')
                C += line.count('C')
                G += line.count('G')
                N += line.count('N')
        GC_count = (G + C)/(A + T + G + C)
        ATGC_count = A + T + G + C
        N_count = N
        list1  = sorted(dict1.items() ,key=lambda d:d[1] ,reverse = True)

    L25, L50, L75, L90 = 0, 0, 0, 0
    N25, N50, N75, N90 = 0, 0, 0, 0
    N25_base, N50_base, N75_base, N90_base = 0, 0, 0, 0
    for key,values in list1:
        if N25_base < Total/4:
            N25_base += values
            L25 += 1
            if N25_base >= Total/4:
                N25 = values
        if N50_base < Total/2:
            N50_base += values
            L50 += 1
            if N50_base >= Total/2:
                N50 = values
        if N75_base < Total*3/4:
            N75_base += values
            L75 += 1
            if N75_base >= Total*3/4:
                N75 = values
        if N90_base < Total*9/10:
            N90_base += values
            L90 += 1
            if N90_base >= Total*9/10:
                N90 = values
    max_contig = list1[0][1]
    min_contig = list1[-1][1]
    print(f'Count\t{count}')
    print(f'Total\t{Total}')
    print(f'MAX\t{max_contig}', f'MIN\t{min_contig}', sep='\n')
    print(f'N25\t{N25}', f'L25\t{L25}', sep='\n')
    print(f'N50\t{N50}', f'L50\t{L50}', sep='\n')
    print(f'N75\t{N75}', f'L75\t{L75}', sep='\n')
    print(f'N90\t{N90}', f'L90\t{L90}', sep='\n')
    print('G + C\t%.2f%%' %(GC_count*100))
    print(f'ATGC_count\t{ATGC_count}')
    print(f'N_count\t{N_count}')
    print('Average\t%.2f' %(Total/len(list1)))
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='输入的基因组文件，即基因组的fasta文件', required=True)
    args = parser.parse_args()
    fa_feature_statistic(args.input)
    
if __name__ == '__main__':
    main()

