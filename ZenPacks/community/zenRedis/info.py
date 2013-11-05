from ZenPacks.community.ConstructionKit.ClassHelper import *

def RedisDBgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class RedisDBInfo(ClassHelper.RedisDBInfo):
    ''''''


