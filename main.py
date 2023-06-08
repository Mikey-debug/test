from requests import Session
from requests.adapters import HTTPAdapter, DEFAULT_POOLSIZE, DEFAULT_RETRIES, DEFAULT_POOLBLOCK


class DNSResolverHTTPSAdapter(HTTPAdapter):
    def __init__(self,
                 common_name,
                 host,
                 pool_connections=DEFAULT_POOLSIZE,
                 pool_maxsize=DEFAULT_POOLSIZE,
                 max_retries=DEFAULT_RETRIES,
                 pool_block=DEFAULT_POOLBLOCK):
        self.__common_name = common_name
        self.__host = host
        super(DNSResolverHTTPSAdapter, self).__init__(
            pool_connections=pool_connections,
            pool_maxsize=pool_maxsize,
            max_retries=max_retries,
            pool_block=pool_block)

    def get_connection(self, url, proxies=None):
        redirected_url = url.replace(self.__common_name, self.__host)
        return super(DNSResolverHTTPSAdapter, self).get_connection(
            redirected_url, proxies=proxies)

    def init_poolmanager(self,
                         connections,
                         maxsize,
                         block=DEFAULT_POOLBLOCK,
                         **pool_kwargs):
        pool_kwargs['assert_hostname'] = self.__common_name
        super(DNSResolverHTTPSAdapter, self).init_poolmanager(
            connections, maxsize, block=block, **pool_kwargs)


common_name = 'www.google.com.hk'
google_dns_host = "114.114.114.114"
url = 'https://animepahe.ru/api?m=search&q=Oshi%20No%20Ko'
my_session = Session()
my_session.mount(url.lower(),
                 DNSResolverHTTPSAdapter(common_name, google_dns_host))
headers = {'Content-Type': 'application/json'}
resp = my_session.get(url, headers=headers)
print resp.code
print resp.text
