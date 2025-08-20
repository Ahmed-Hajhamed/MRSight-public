from matplotlib.patches import FancyArrowPatch

class Arrow(FancyArrowPatch):
    def __init__(self, posA, posB, *, path = None, arrowstyle ="->" , connectionstyle = None, patchA = None, patchB = None, shrinkA = 0, shrinkB = 0, mutation_scale = 15, mutation_aspect = None, **kwargs):
        super().__init__(posA, posB, path=path, arrowstyle=arrowstyle, connectionstyle=connectionstyle, patchA=patchA, patchB=patchB, shrinkA=shrinkA, shrinkB=shrinkB, mutation_scale=mutation_scale, mutation_aspect=mutation_aspect, **kwargs)
        self.posA = posA
        self.posB = posB

    def set_positions(self, posA, posB):
        self.posA = posA
        self.posB = posB
        return super().set_positions(posA, posB)
    