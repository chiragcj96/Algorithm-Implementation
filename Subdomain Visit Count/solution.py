class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        dict= {}
        for i in range(len(cpdomains)):

            cpdomains[i].split()
            splited = cpdomains[i].split()
            number = splited[0]
            domain = splited[-1]
            partDomain = domain.split(".", 1)
            subDomain = partDomain[-1].split(".", 1)
            
            dict[domain] = dict.get(domain, 0) + int(number)
            dict[partDomain[-1]] = dict.get(partDomain[-1], 0) + int(number)
            if subDomain[-1]!=partDomain[-1]:
                dict[subDomain[-1]] = dict.get(subDomain[-1], 0) + int(number)
            
            # print(number, domain, partDomain[-1], subDomain[-1])
            print dict       
        result = []
        for key in dict:
            result.append(str(dict[key]) + " " + str(key))
        return result
            
            
            
            
        