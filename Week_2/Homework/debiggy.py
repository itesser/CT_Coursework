def best_today(pb, project):
    verify = [pb, project]
    for i in range(len(verify)):
        verify[i] = verify[i].strip('abcde').replace('.','')
    if int(verify[1]) > int(verify[0]) or ord(project[-1:]) > ord(self.pb[-1:]):
        return project

print(best_today('5.9', '5.10a'))