import random
import copy


def ProbSim(pList):
    S = sum(pList)
    npList = [x / S for x in pList]
    # print(NP/S,TP/S)
    D = random.uniform(0, 1)
    # print(D)
    currThreshold = 0
    for index, item in enumerate(npList):
        currThreshold += item
        if D < currThreshold:
            # print(index)
            return index

def ProbSim2(pList):
    if len(pList)<2:
        print('ERROR not enough samples')
        return [-1,-1]
    result_a=0
    result_b=0
    while result_a == result_b:
        result_a = ProbSim(pList)
        result_b = ProbSim(pList)
    return [result_a,result_b]


ProbSim(pList=[0.15, 0.85])


class Sample:
    genes = [0,0,0]
    lineage = ['','','']
    fit = 0
    id=0
    parent_2g_id=0
    parent_1g_id=0

    def __init__(self,_id, _parent_2g=None, _parent_1g=None):
        self.id=_id
        print('new sample id=',self.id+1,end=', ')
        if _parent_1g and _parent_2g:
            _1g = random.randint(0,2)
            self.genes = _parent_2g.genes[:]
            self.lineage = _parent_2g.lineage[:]

            self.genes[_1g]=_parent_1g.genes[_1g]
            self.lineage[_1g] = _parent_1g.lineage[_1g]
            #

            if ProbSim([0.15, 0.85]) == 0:
                # print('mutation triggered',end=', ')
                _Mg = random.randint(0, 2)
                self.genes[_Mg] = random.randint(1,10)
                self.lineage[_Mg] = 'm'

            self.fitness()

            print('\t',"with genes:", self.genes,'   \t', 'lineage:', self.lineage,'\t', 'fitness:',self.fit)

            self.parent_2g_id=_parent_2g.id
            self.parent_1g_id=_parent_1g.id

    def fitness(self):
        self.fit = 0.5*self.genes[0] +1.25*self.genes[1]+2.0*self.genes[2]
        return self.fit


class Generation:
    def __init__(self, _parent_a=None, _parent_b=None):
        self.samples = []
        self.fSUM = 0
        if _parent_a and _parent_b:
            for i in range(0,6):
                # print(i)
                if i <3:
                    self.samples.append(Sample(i, _parent_a, _parent_b))

                else:
                    self.samples.append(Sample(i, _parent_b, _parent_a))

                self.fSUM+=self.samples[i].fit

    def add_pop(self,sample):
        self.samples.append(sample)
        self.fSUM += self.samples[len(self.samples)-1].fitness()

    def printTB(self):
        print('PpoNumber', '\t','Gene1', '\t','Gene2','\t', 'Gene3','\t', 'Fitness','\t', 'Prob')
        for item in self.samples:
            print('\t', item.id+1,'\t','\t', item.genes[0],'  \t', item.genes[1],'  \t', item.genes[2],'  \t', item.fit,'\t','\t', '%1.3f' % (item.fit / self.fSUM))

    def reproduce(self):
        [a_id,b_id] = ProbSim2([x.fit for x in self.samples])


        parent_a = copy.copy(self.samples[a_id])
        parent_a.lineage = ['a','a','a']
        parent_b = copy.copy(self.samples[b_id])
        parent_b.lineage = ['b', 'b', 'b']
        print('selected parents: a =', a_id + 1,parent_a.genes,'\t b =', b_id + 1,parent_b.genes, )
        newGen = Generation(_parent_a=parent_a,_parent_b=parent_b)
        return newGen



simGen = Generation()

newpop = Sample(0)
newpop.genes=[7, 6, 2]
simGen.add_pop(newpop)

newpop = Sample(1)
newpop.genes=[4 , 5, 6]
simGen.add_pop(newpop)

newpop = Sample(2)
newpop.genes=[6 , 1, 2]
simGen.add_pop(newpop)

newpop = Sample(3)
newpop.genes=[2 , 2, 7]
simGen.add_pop(newpop)

newpop = Sample(4)
newpop.genes=[5 , 8, 8]
simGen.add_pop(newpop)

newpop = Sample(5)
newpop.genes=[6 , 9, 10]
simGen.add_pop(newpop)


randomseed = 2902
if randomseed:
    random.seed(randomseed)
    print('\nSimulation WITH random seed:',randomseed)
else:
    print('\nSimulation WITHOUT random seed.')

print('initial Generation:')
# newG = Generation(parent_a, parent_b)
simGen.printTB()


print('\n1st Generation')
Gen1 = simGen.reproduce()
Gen1.printTB()

print('\n2nd Generation')
Gen2 = Gen1.reproduce()
Gen2.printTB()
