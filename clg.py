class   Vector_shuffle_set:
    def __init__(self):
        self.mux=1664525
        self.increment=1013904223
        self.module=2**32
        self.vector=[]

    def lcg(self,lenght,seed):
        for i   in  range(lenght):
            seed=(self.mux*seed+self.increment)%self.module
            self.vector.append(seed)
        return  self.vector

    def run_lcg(self,vector_len,initial_seed):
        return  self.lcg(vector_len,initial_seed)
