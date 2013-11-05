from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *               
                            
RedisDefinition = type('RedisDefinition', (BasicDefinition,), {
        'version' : Version(1, 1, 0),
        'zenpackbase': "zenRedis",
        'component' : 'RedisDB',
        'componentData' : {
                          'singular': 'Redis DB',
                          'plural': 'Redis DBs',
                          'displayed': 'hostname', # component field in Event Console
                          'primaryKey': 'hostname',
                          'properties': { 
                                        # Basic settings
                                        'hostname' : addProperty('Hostname or IP','Basic','id', switch='-H', override=True, isReference=True),
                                        'port' : addProperty('Port','Basic','4730', switch='-p',optional='false'),
                                        'eventClass' : getEventClass('/App/Redis'),
                                        },
                          },
        'cmdFile' : 'check_redis.pl',
        'addManual' : True,
        'createDS' :  False
        }
)

addDefinitionSelfComponentRelation(RedisDefinition,
                          'redisdb', ToOne, 'ZenPacks.community.zenRedis.RedisDB','port',
                          'ipservice',  ToOne, 'Products.ZenModel.IpService', 'port',
                          'IP Service', 'port')
