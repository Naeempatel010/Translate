import tornado.ioloop
import tornado.web
from googletrans import Translator
port = 8888
class Translator_api(tornado.web.RequestHandler):
	def post(self):
		try:
			from_lang = self.get_argument('from',True)
			to_lang = self.get_argument('to',True)
			input_seq = self.get_argument('input',True)
			#print(type(from_lang))
			#print(to_lang)
			#print(type(input_seq)
			output_d={}
			trans  = Translator()
			output = trans.translate(input_seq,dest = to_lang)
			#print(output)
			output_d['success'] = 1
			output_d["output"] = output.pronunciation
			output_d["text"] = output.text
			print(output_d)
			self.write(output_d)
	
		except AssertionError:
			output_d["success"] = 0 
			self.write(output_d)
		
def make_app():
	return tornado.web.Application([(r"/translate", Translator_api)])


if __name__ == "__main__":
	app = make_app()
	app.listen(port)
	tornado.ioloop.IOLoop.current().start()

		
						
		
