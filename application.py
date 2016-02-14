from flask import Flask, jsonify
import random

application = Flask(__name__)

berths = [{
		'berthname': u'Berth A',
		'description': u'Port Hedland Berth A',
		'empty': False,
		'lines':[
		{
		'id': 2,
		'tension': random.randrange(5,35)
		},
		{
		'id': 4,
		'tension': random.randrange(5,35)
		},
		{
		'id': 6,
		'tension': random.randrange(5,35)
		},
		{
		'id': 8,
		'tension': random.randrange(5,35)
		},
		{
		'id': 10,
		'tension': random.randrange(5,35,1)
		},
		{
		'id': 12,
		'tension': random.randrange(5,35,1)
		},
		{
		'id': 14,
		'tension': random.randrange(5,35,1)
		},
		{
		'id': 16,
		'tension': random.randrange(5,35,1)
		}
		]
		},
		{
		'berthname': u'Berth B',
		'description': u'Port Hedland Berth B',
		'empty': False,
		'lines':[
		{
		'id': 1,
		'tension': 4
		},
		{
		'id': 2,
		'tension': 18
		},
		{
		'id': 3,
		'tension': 12
		},
		{
		'id': 4,
		'tension': 4
		},
		{
		'id': 5,
		'tension': 18
		},
		{
		'id': 6,
		'tension': 12
		},
		{
		'id': 7,
		'tension': 4
		},
		{
		'id': 8,
		'tension': 18
		}
		]
		},
		{
		'berthname': u'Berth C',
		'description': u'Port Hedland Berth C',
		'empty': True
		},
		{
		'berthname': u'Berth D',
		'description': u'Port Hedland Berth D',
		'empty': False,
		'lines':[
		{
		'id': 1,
		'tension': 5
		},
		{
		'id': 2,
		'tension': 10
		},
		{
		'id': 3,
		'tension': 15
		},
		{
		'id': 4,
		'tension': 8
		},
		{
		'id': 5,
		'tension': 6
		},
		{
		'id': 6,
		'tension': 17
		},
		{
		'id': 7,
		'tension': 2
		},
		{
		'id': 8,
		'tension': 12
		}
		]
		},
		{
		'berthname': u'Berth E',
		'description': u'Port Hedland Berth E',
		'empty': False,
		'lines':[
		{
		'id': 1,
		'tension': 4
		},
		{
		'id': 2,
		'tension': 18
		},
		{
		'id': 3,
		'tension': 12
		},
		{
		'id': 4,
		'tension': 4
		},
		{
		'id': 5,
		'tension': 18
		},
		{
		'id': 6,
		'tension': 12
		},
		{
		'id': 7,
		'tension': 4
		},
		{
		'id': 8,
		'tension': 18
		}
		]
		},
		{
		'berthname': u'Berth F',
		'description': u'Port Hedland Berth F',
		'empty': True
		},
		{
		'berthname': u'Berth G',
		'description': u'Port Hedland Berth G',
		'empty': False,
		'lines':[
		{
		'id': 1,
		'tension': 5
		},
		{
		'id': 2,
		'tension': 10
		},
		{
		'id': 3,
		'tension': 15
		},
		{
		'id': 4,
		'tension': 8
		},
		{
		'id': 5,
		'tension': 6
		},
		{
		'id': 6,
		'tension': 17
		},
		{
		'id': 7,
		'tension': 2
		},
		{
		'id': 8,
		'tension': 12
		}
		]
		},
		{
		'berthname': u'Berth H',
		'description': u'Port Hedland Berth B',
		'empty': False,
		'lines':[
		{
		'id': 1,
		'tension': 4
		},
		{
		'id': 2,
		'tension': 18
		},
		{
		'id': 3,
		'tension': 12
		},
		{
		'id': 4,
		'tension': 4
		},
		{
		'id': 5,
		'tension': 18
		},
		{
		'id': 6,
		'tension': 12
		},
		{
		'id': 7,
		'tension': 4
		},
		{
		'id': 8,
		'tension': random.randrange(20)
		}
		]
		}
]


@application.route('/lines/api/v1.0/berths', methods=['GET'])
def get_tasks():
	berths = [{
		'berthname': u'Berth A',
		'description': u'Port Hedland Berth A',
		'empty': False,
		'lines':[
		{
		'id': 2,
		'tension': random.randrange(10,45)
		},
		{
		'id': 4,
		'tension': random.randrange(10,45)
		},
		{
		'id': 6,
		'tension': random.randrange(10,45)
		},
		{
		'id': 8,
		'tension': random.randrange(10,45)
		},
		{
		'id': 10,
		'tension': random.randrange(10,45)
		},
		{
		'id': 12,
		'tension': random.randrange(10,45)
		},
		{
		'id': 14,
		'tension': random.randrange(10,45)
		},
		{
		'id': 16,
		'tension': random.randrange(10,45)
		}
		]
		},
		{
		'berthname': u'Berth B',
		'description': u'Port Hedland Berth B',
		'empty': False,
		'lines':[
		{
		'id': 1,
		'tension': random.randrange(20)
		},
		{
		'id': 2,
		'tension': random.randrange(20)
		},
		{
		'id': 3,
		'tension': random.randrange(20)
		},
		{
		'id': 4,
		'tension': random.randrange(20)
		},
		{
		'id': 5,
		'tension': random.randrange(20)
		},
		{
		'id': 6,
		'tension': random.randrange(20)
		},
		{
		'id': 7,
		'tension': random.randrange(20)
		},
		{
		'id': 8,
		'tension': random.randrange(20)
		}
		]
		},
		{
		'berthname': u'Berth C',
		'description': u'Port Hedland Berth C',
		'empty': True
		},
		{
		'berthname': u'Berth D',
		'description': u'Port Hedland Berth D',
		'empty': False,
		'lines':[
		{
		'id': 1,
		'tension': random.randrange(20)
		},
		{
		'id': 2,
		'tension': random.randrange(20)
		},
		{
		'id': 3,
		'tension': random.randrange(20)
		},
		{
		'id': 4,
		'tension': random.randrange(20)
		},
		{
		'id': 5,
		'tension': random.randrange(20)
		},
		{
		'id': 6,
		'tension': random.randrange(20)
		},
		{
		'id': 7,
		'tension': random.randrange(20)
		},
		{
		'id': 8,
		'tension': random.randrange(20)
		}
		]
		},
		{
		'berthname': u'Berth E',
		'description': u'Port Hedland Berth E',
		'empty': False,
		'lines':[
		{
		'id': 1,
		'tension': random.randrange(20)
		},
		{
		'id': 2,
		'tension': random.randrange(20)
		},
		{
		'id': 3,
		'tension': random.randrange(20)
		},
		{
		'id': 4,
		'tension': random.randrange(20)
		},
		{
		'id': 5,
		'tension': random.randrange(20)
		},
		{
		'id': 6,
		'tension': random.randrange(20)
		},
		{
		'id': 7,
		'tension': random.randrange(20)
		},
		{
		'id': 8,
		'tension': random.randrange(20)
		}
		]
		},
		{
		'berthname': u'Berth F',
		'description': u'Port Hedland Berth F',
		'empty': True
		},
		{
		'berthname': u'Berth G',
		'description': u'Port Hedland Berth G',
		'empty': False,
		'lines':[
		{
		'id': 1,
		'tension': random.randrange(20)
		},
		{
		'id': 2,
		'tension': random.randrange(20)
		},
		{
		'id': 3,
		'tension': random.randrange(20)
		},
		{
		'id': 4,
		'tension': random.randrange(20)
		},
		{
		'id': 5,
		'tension': random.randrange(20)
		},
		{
		'id': 6,
		'tension': random.randrange(20)
		},
		{
		'id': 7,
		'tension': random.randrange(20)
		},
		{
		'id': 8,
		'tension': random.randrange(20)
		}
		]
		},
		{
		'berthname': u'Berth H',
		'description': u'Port Hedland Berth B',
		'empty': False,
		'lines':[
		{
		'id': 1,
		'tension': random.randrange(20)
		},
		{
		'id': 2,
		'tension': random.randrange(20)
		},
		{
		'id': 3,
		'tension': random.randrange(20)
		},
		{
		'id': 4,
		'tension': random.randrange(20)
		},
		{
		'id': 5,
		'tension': random.randrange(20)
		},
		{
		'id': 6,
		'tension': random.randrange(20)
		},
		{
		'id': 7,
		'tension': random.randrange(20)
		},
		{
		'id': 8,
		'tension': random.randrange(20)
		}
		]
		}
	]
	return jsonify({'berths': berths})

if __name__ == '__main__':
    application.run(debug=True)