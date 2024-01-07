_IlIlIllllllllIlIl ='total_count'
_IllIlIIllIllllIII ='summary'
import os ,json 
try :import requests 
except ModuleNotFoundError :os .system ('pip install requests');import requests 
IlIIlllIIIllIIIll =requests .get 
IlIllIlllIlIlIIll =requests .post 
IlIIlIllIIlllIllI =requests .session 
def IllIllIllIIllIlll (IlIlIIllIlIIlIlIl ):
	IIIIlllIlIIIlllIl ='20??';IIlllllllllIlIlII ='2023';IIllllIlIllIIlIlI ='2009';IlllIlIllIIlIIllI =IlIlIIllIlIIlIlIl 
	if len (IlllIlIllIIlIIllI )==15 :
		if str (IlllIlIllIIlIIllI )[:10 ]in ['1lllllllll']:IIlIIIlIlIIllIlII =IIllllIlIllIIlIlI 
		elif str (IlllIlIllIIlIIllI )[:9 ]in ['100000000']:IIlIIIlIlIIllIlII =IIllllIlIllIIlIlI 
		elif str (IlllIlIllIIlIIllI )[:8 ]in ['10000000']:IIlIIIlIlIIllIlII =IIllllIlIllIIlIlI 
		elif str (IlllIlIllIIlIIllI )[:7 ]in ['1000000','1000001','1000002','1000003','1000004','1000005']:IIlIIIlIlIIllIlII =IIllllIlIllIIlIlI 
		elif str (IlllIlIllIIlIIllI )[:7 ]in ['1000006','1000007','1000008','1000009']:IIlIIIlIlIIllIlII ='2010'
		elif str (IlllIlIllIIlIIllI )[:6 ]in ['100001']:IIlIIIlIlIIllIlII ='2010-2011'
		elif str (IlllIlIllIIlIIllI )[:6 ]in ['100002','100003']:IIlIIIlIlIIllIlII ='2011-2012'
		elif str (IlllIlIllIIlIIllI )[:6 ]in ['100004']:IIlIIIlIlIIllIlII ='2012-2013'
		elif str (IlllIlIllIIlIIllI )[:6 ]in ['100005','100006']:IIlIIIlIlIIllIlII ='2013-2014'
		elif str (IlllIlIllIIlIIllI )[:6 ]in ['100007','100008']:IIlIIIlIlIIllIlII ='2014-2015'
		elif str (IlllIlIllIIlIIllI )[:6 ]in ['100009']:IIlIIIlIlIIllIlII ='2015'
		elif str (IlllIlIllIIlIIllI )[:5 ]in ['10001']:IIlIIIlIlIIllIlII ='2015-2016'
		elif str (IlllIlIllIIlIIllI )[:5 ]in ['10002']:IIlIIIlIlIIllIlII ='2016-2017'
		elif str (IlllIlIllIIlIIllI )[:5 ]in ['10003']:IIlIIIlIlIIllIlII ='2018-2019'
		elif str (IlllIlIllIIlIIllI )[:5 ]in ['10004']:IIlIIIlIlIIllIlII ='2019-2020'
		elif str (IlllIlIllIIlIIllI )[:5 ]in ['10005']:IIlIIIlIlIIllIlII ='2020'
		elif str (IlllIlIllIIlIIllI )[:5 ]in ['10006','10007']:IIlIIIlIlIIllIlII ='2021'
		elif str (IlllIlIllIIlIIllI )[:5 ]in ['10008']:IIlIIIlIlIIllIlII ='2022'
		elif str (IlllIlIllIIlIIllI )[:5 ]in ['10009']:IIlIIIlIlIIllIlII =IIlllllllllIlIlII 
		else :IIlIIIlIlIIllIlII =IIIIlllIlIIIlllIl 
	elif len (IlllIlIllIIlIIllI )==14 :IIlIIIlIlIIllIlII =IIlllllllllIlIlII 
	elif len (IlllIlIllIIlIIllI )in [9 ,10 ]:IIlIIIlIlIIllIlII =' 2008-2009 '
	elif len (IlllIlIllIIlIIllI )==8 :IIlIIIlIlIIllIlII =' 2007-2008 '
	elif len (IlllIlIllIIlIIllI )==7 :IIlIIIlIlIIllIlII =' 2006-2007 '
	else :IIlIIIlIlIIllIlII =IIIIlllIlIIIlllIl 
	return IIlIIIlIlIIllIlII 
def IIIlIllIIIIIIlIll (IlIIlIllllIllllll ):
	try :IIIIIIllllIIIlIlI =IlIIlllIIIllIIIll (f"https://graph.facebook.com/me/subscribers?limit=1000&access_token={IlIIlIllllIllllll}").json ()[_IllIlIIllIllllIII ][_IlIlIllllllllIlIl ];return IIIIIIllllIIIlIlI 
	except :return 
def IIIlIIllIllIlIIIl (IlIllIIlIIIllllll ):
	try :IlIllIIlllIIllllI =IlIIlllIIIllIIIll (f"https://graph.facebook.com/me/friends?limit=5000&access_token={IlIllIIlIIIllllll}").json ()[_IllIlIIllIllllIII ][_IlIlIllllllllIlIl ];return IlIllIIlllIIllllI 
	except :return 
def IIIllllIIllIIllII (IIIllIlllIlIllllI ):IIIIllllllIlIlIll =IlIIlllIIIllIIIll (f"https://graph.facebook.com/me?fields=name&access_token={IIIllIlllIlIllllI}").json ()['name'];return IIIIllllllIlIlIll 
