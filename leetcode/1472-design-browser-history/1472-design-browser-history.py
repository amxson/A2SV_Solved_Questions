class Node:
    def __init__(self,url):
        self.url = url
        self.prev = None
        self.next = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Node(homepage)
    def visit(self, url: str) -> None:
        self.new = Node(url)
        self.cur.next = self.new
        self.new.prev = self.cur
        self.cur = self.new
    def back(self, steps: int) -> str:
        while self.cur.prev and steps>0:
            self.cur = self.cur.prev
            steps-=1
        return(self.cur.url)
    def forward(self, steps: int) -> str:
        while self.cur.next and steps>0:
            self.cur = self.cur.next
            steps-=1
        return(self.cur.url)
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)