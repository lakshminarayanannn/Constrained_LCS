import sys
input = sys.stdin.readline
I = lambda : list(map(int,input().split()))

from collections import defaultdict


class TrieNode():

    def __init__(self):
        self.children = defaultdict(str)
        self.failureLink= ""
        self.terminating = False
        self.word=""
        self.num=-1

class Trie():

    def __init__(self):
        self.root = TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):

        root = self.root

        for i in word:
            if i not in root.children:
                root.children[i] = TrieNode()
            root = root.children[i]

        root.terminating = True

    def search(self, word , prefix=0):

        root = self.root

        for i in word:
            if not root:
                return False
            root = root.children[i]

        if prefix:
            if root :
               return root
            else:
               return False
        else:
            return True if (root and root.terminating) else False

    def delete(self, word):

        root = self.root

        for i in word:
            if not root:
                print ("Word not found")
                return -1
            root = root.children[i]

        if not root:
            print ("Word not found")
            return -1
        else:
            root.terminating = False
            return 0

    def update(self, old_word, new_word):
        val = self.delete(old_word)
        if val == 0:
            self.insert(new_word)


if __name__ == "__main__":

    strings = ["CAT", "ATC", "ACC","GCG"]
    t = Trie()
    for word in strings:
        t.insert(word)
    ct = 0
    pre=[]
    t.root.failureLink=t.root
    que=[[t.root,""]]
    while que:
        root,word = que.pop();root.word=word
        if(root.terminating==False):
            root.num=ct
            pre.append(root);ct+=1
        for i in root.children:
            if root.children[i]:
                que.append([root.children[i],word+i])
        for x in range(1,len(word)+1):
            k=t.search(word[x:],1)
            if k:
                root.failureLink=k
                break
    lambd = [[-1]*26 for i in range(ct)]
    lambd[0]=[0]*26
    que=[[t.root]]
    while que:
        root, = que.pop()
        for i in root.children:
            if root.children[i]:
                que.append([root.children[i]])
            if root.terminating==False and root.children[i]:
                lambd[root.num][ord(i)-ord('A')]=root.children[i].num

    for i in range(ct):
        pre[i]=pre[i].failureLink

    for i in range(1,ct):
        for j in range(26):
            if lambd[i][j]==-1:
                lambd[i][j]=lambd[pre[i].num][j]

    x=input().strip()
    y=input().strip()
    n,m=len(x),len(y)
    x="0"+x;y="0"+y
    ans=[[[0]*ct for i in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            for k in range(ct):
                ans[i][j][k]=max(ans[i-1][j][k],ans[i][j-1][k])
            if x[i]==y[j]:
                for kk in range(ct):
                    tt=lambd[kk][ord(x[i])-ord("A")]
                    ans[i][j][tt]=max(ans[i-1][j-1][tt],1+ans[i-1][j-1][kk])
    print(max(ans[n][m]))
    ix=ans[n][m].index(max(ans[n][m]))
    print(ans[n][m])
    def back(i,j,k):
        if i==0 or j==0:
            return 
        if x[i]==y[j]:
            if ans[i][j][k]==ans[i-1][j-1][k]:
                back(i-1,j-1,k)
            else:
                ppp=max(ans[i][j])
                xx=ans[i][j].index(ppp)
                back(i-1,j-1,xx)
                print(x[i],end='')
        elif ans[i-1][j][k]>ans[i][j-1][k]:
            back(i-1,j,k)
        else:
            back(i,j-1,k)
    back(n,m,ix)
    """
    query = "GCATCGGGPPCAT"
    cr=t.root
    for i in query:
        if cr.children.get(i,""):
            cr=cr.children[i]
            if cr and cr.terminating:
                print(cr.word)
                cr=cr.failureLink
        else:
            while cr!=t.root and (not cr.children.get(i,"")):
                cr=cr.failureLink
            if i in cr.children:
                cr=cr.children[i]
                if cr and cr.terminating:
                    print(cr.word)
                    cr=cr.failureLink
    """s