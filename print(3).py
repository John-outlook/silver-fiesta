
from pandas_datareader import data as web
spx = web.DataReader('ˆGSPC', data_source='yahoo',
end='2015-12-31')
