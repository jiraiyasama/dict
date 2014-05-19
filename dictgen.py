import optparse,datetime
import hashlib

chars=[
                '0','1','2','3','4','5','6','7','8','9',
                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                '`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','[','}',']','\\','|',':',':','"','\'','<',',','>','.','?','/'
        ]

def sha512dict(chars,hashkey):
    for char0 in chars:
        if hashlib.sha512(char0).hexdigest()==hashkey:
            return "The key is %s"%(char0)
            break
        for char1 in chars:
            key=char0+char1
            if hashlib.sha512(key).hexdigest()==hashkey:
                return "The key is %s"%(key)
                break
            for char2 in chars:
                key=char0+char1+char2
                if hashlib.sha512(key).hexdigest()==hashkey:
                    return "The key is %s"%(key)
                    break
                for char3 in chars:
                    key=char0+char1+char2+char3
                    if hashlib.sha512(key).hexdigest()==hashkey:
                        return "The key is %s"%(key)
                        break
                    for char4 in chars:
                        key=char0+char1+char2+char3+char4
                        if hashlib.sha512(key).hexdigest()==hashkey:
                            return "The key is %s"%(key)
                            break
                        for char5 in chars:
                            key=char0+char1+char2+char3+char4+char5
                            if hashlib.sha512(key).hexdigest()==hashkey:
                                return "The key is %s"%(key)
                                break
                            for char6 in chars:
                                key=char0+char1+char2+char3+char4+char5+char6
                                if hashlib.sha512(key).hexdigest()==hashkey:
                                    return "The key is %s"%(key)
                                    break

if __name__=='__main__':
    optParser=optparse.OptionParser()
    optParser.add_option('-f','--filename',dest='hashfile')
    (options,args)=optParser.parse_args()
    print options['hashfile']