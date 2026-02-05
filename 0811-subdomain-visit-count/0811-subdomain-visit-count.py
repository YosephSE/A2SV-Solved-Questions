class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        for i in cpdomains:
            visits, domain = i.split()
            visits = int(visits)
            domains = domain.split(".")
            for j in range(len(domains)):
                dom = '.'.join(domains[j:])
                count[dom] = count.get(dom, 0) + visits
        res = []
        for i in count:
            res.append(f'{count[i]} {i}')
        return res
                

        

        