import pygame


def createrect(l):
    ll = []
    for i in range(len(l)):
        ll.append(('testrect'+str(i)+'=pygame.Rect('+str(l[i])+',(64,64))'))
    return ll



