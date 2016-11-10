from django.db import connection


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        sql_list = connection.queries
        len_sql_list = len(sql_list)
        total_time = float()
        for n in xrange(len_sql_list):
            total_time = total_time + float(sql_list[n]['time'])
        if getattr(response, "content", None):
            response.content = response.content.replace('</body>', '<div style="padding-left:1%">' +
                                                        'number of SQL requests: ' + str(len_sql_list) + '<br>'
                                                        + 'total time: ' + str(total_time) + '</div><br></body>')

        return response