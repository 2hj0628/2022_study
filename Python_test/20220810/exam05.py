
height=int(input('당신의 키(cm)는?'))
# m_height or cm_height
m_height=height // 100        #1m=100cm
cm_height=height % 100

print('당신의 키는',m_height,'m',cm_height,'cm 입니다.')