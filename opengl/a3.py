import numpy as np
import math


def fun(core, prosurface, vx, vy, vz, T):  #计算三维平面转二维平面
    vpt = prosurface[0] * prosurface[0] + prosurface[1] * prosurface[1] + prosurface[2] * prosurface[2]
    t = ((core[0] - vx) * prosurface[0] + (core[1] - vy) * prosurface[1] + (core[2] - vz) * prosurface[2]) / vpt
    x = vx + prosurface[0] * t
    y = vy + prosurface[1] * t
    z = vz + prosurface[2] * t
    old = np.mat([x, y, z, 1])
    new = old * T
    res = new.getA()
    return [res[0][0], res[0][2]]

def getarea(twoD):
    a = twoD[0]
    b = twoD[1]
    c = twoD[2]
    ab = np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    ac = np.sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)
    bc = np.sqrt((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)
    s = (ab + ac + bc) / 2.0
    area = np.sqrt(s * (s - ab) * (s - ac) * (s - bc))
    return area

class A3:
    def __init__(self, obj, vpoint, area, T, visface):
        self.obj = obj
        self.core = obj.bbox_center[:]  # 图形中心
        self.vp = vpoint  # 视点位置
        self.prosurface = np.array(
            [self.vp[0] - self.core[0], self.vp[1] - self.core[1], self.vp[2] - self.core[2]])  # 投影面法向量
        self.area = area
        self.T = T
        self.visface = visface
        self.p = []  #概率
        self.h = 0  #香农熵

    def getshannon(self):
        visVertices = self.obj.vertices[:]
        for i in range(len(self.visface)):
            twoD = []
            v1index = self.visface[i][0] - 1
            v2index = self.visface[i][1] - 1
            v3index = self.visface[i][2] - 1
            vx1 = visVertices[v1index][0]
            vy1 = visVertices[v1index][1]
            vz1 = visVertices[v1index][2]
            twoD.append(fun(self.core, self.prosurface, vx1, vy1, vz1, self.T))
            vx2 = visVertices[v2index][0]
            vy2 = visVertices[v2index][1]
            vz2 = visVertices[v2index][2]
            twoD.append(fun(self.core, self.prosurface, vx2, vy2, vz2, self.T))
            vx3 = visVertices[v3index][0]
            vy3 = visVertices[v3index][1]
            vz3 = visVertices[v3index][2]
            twoD.append(fun(self.core, self.prosurface, vx3, vy3, vz3, self.T))
            currentarea = getarea(twoD)
            self.p.append(currentarea / self.area)

        for curp in self.p:
            self.h += -curp * math.log(curp, 2)
        print("shang")
        print(self.h)


