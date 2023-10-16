from diagrams import Diagram
import graphviz
from diagrams.aws.compute import EC2 
from diagrams.aws.network import ELB, VPC
from diagrams.aws.database import RDS



with Diagram("WEB Service", show=False):
    ELB('elb') >> EC2("web") >> RDS("userdb")
    # doctest_mark_exe()
    
if __name__ == "__main__":
    dot = graphviz.Digraph()
    print(dot.subgraph)
