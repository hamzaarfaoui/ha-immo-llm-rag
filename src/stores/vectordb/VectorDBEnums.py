from enum import Enum

class VectorDBEnums(Enum):
    QDRANT = "QDRANT" # our DB

class DistanceMethodEnums(Enum):
    COSINE = "cosine"
    DOT = "dot"