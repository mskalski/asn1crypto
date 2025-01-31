# coding: utf-8
from __future__ import unicode_literals, division, absolute_import, print_function

import unittest
import os

from asn1crypto import keys, core, util

from .unittest_data import data_decorator, data
from ._unittest_compat import patch

patch()

tests_root = os.path.dirname(__file__)
fixtures_dir = os.path.join(tests_root, 'fixtures')


@data_decorator
class KeysTests(unittest.TestCase):

    def test_parse_rsa_private_key(self):
        with open(os.path.join(fixtures_dir, 'keys/test-der.key'), 'rb') as f:
            key = keys.RSAPrivateKey.load(f.read())

        self.assertEqual(
            'two-prime',
            key['version'].native
        )
        self.assertEqual(
            23903990516906431865559598284199534387004799030432486061102966678620221767754702651554142956492614440585611990224871381291841413369032752409360196079700921141819811294444393525264295297988924243231844876926173670633422654261873814968313363171188082579071492839040415373948505938897419917635370450127498164824808630475648771544810334682447182123219422360569466851807131368135806769502898151721274383486320505905826683946456552230958810028663378886363555981449715929872558073101554364803925363048965464124465016494920967179276744892632783712377912841537032383450409486298694116013299423220523450956288827030007092359007,  # noqa
            key['modulus'].native
        )
        self.assertEqual(
            65537,
            key['public_exponent'].native
        )
        self.assertEqual(
            9979296894007354255484849917690758820642557661666429934720496335307525025035760937280030384204921358841911348590147260206368632524783497961763507098900120579828036636037636859350155169644276779450131617753331883188587268575077705380671279069284616924232052795766448946873233783789819627790465470123569125678598045748629782316184667685110712273519313310937077963014676074966877849272992367512921997850502687035430136911690081438185238817835171119161013656103255853961444458012340770881411877222316871444386486841632394098449378506206645681449475758856053641206175913163492821894709155329556294181613669730336931773953,  # noqa
            key['private_exponent'].native
        )
        self.assertEqual(
            166647390172913547327716251713919741459272587597255782032652236515036001974461323181989715320980256918783849999012066159723695368018857439366733087649658067943054926668058248612521531843495934099419046629521378187012692776633310821178903471282399402138521150042979117060141563972064613977168440186057796106743,  # noqa
            key['prime1'].native
        )
        self.assertEqual(
            143440533284701431115857974625778819273481773744021067505004499855263691219807413711274106281992493130281690570930126889424222979194828112331057105055939481042398415265558356642606674863401518188395487842736496447305100392269029249928750130190700690239916449523411304928539660679996452045625683879143320460249,  # noqa
            key['prime2'].native
        )
        self.assertEqual(
            109414079859473229289779858629449815451592843305649008118818271892297238643195390011716060554289324731958287404176117228233683079641781234394481865640434212819044363330635799312574408253258259431525735957118503776629524657609514187779529692628749620437591384488141789034909003405007374076072765197764330205487,  # noqa
            key['exponent1'].native
        )
        self.assertEqual(
            39361498857013145813625735320048312950154816653378623953034178027634194773898965899927575680536994315500952488328843279054659597751495930118280223039291020752651068863936425009698924893471060669547041417272275998418220630400632040385105243470857091616562513209775072216226822370097138922876120342440353924609,  # noqa
            key['exponent2'].native
        )
        self.assertEqual(
            109796662729796355370195012683418958273962986010546166376879205603219777065076464250440708895625560840314914603409569660942497623175203159192440744329997446961447023349392064212216532091513743978251892999757210494211477167363008686808094766092274115601607346901935491774285446659775729268493276413171032997893,  # noqa
            key['coefficient'].native
        )
        self.assertEqual(
            None,
            key['other_prime_infos'].native
        )

    def test_parse_rsa_private_key_no_spec(self):
        with open(os.path.join(fixtures_dir, 'keys/test-der.key'), 'rb') as f:
            key = core.Asn1Value.load(f.read())

        self.assertEqual(
            0,
            key[0].native
        )
        self.assertEqual(
            23903990516906431865559598284199534387004799030432486061102966678620221767754702651554142956492614440585611990224871381291841413369032752409360196079700921141819811294444393525264295297988924243231844876926173670633422654261873814968313363171188082579071492839040415373948505938897419917635370450127498164824808630475648771544810334682447182123219422360569466851807131368135806769502898151721274383486320505905826683946456552230958810028663378886363555981449715929872558073101554364803925363048965464124465016494920967179276744892632783712377912841537032383450409486298694116013299423220523450956288827030007092359007,  # noqa
            key[1].native
        )
        self.assertEqual(
            65537,
            key[2].native
        )
        self.assertEqual(
            9979296894007354255484849917690758820642557661666429934720496335307525025035760937280030384204921358841911348590147260206368632524783497961763507098900120579828036636037636859350155169644276779450131617753331883188587268575077705380671279069284616924232052795766448946873233783789819627790465470123569125678598045748629782316184667685110712273519313310937077963014676074966877849272992367512921997850502687035430136911690081438185238817835171119161013656103255853961444458012340770881411877222316871444386486841632394098449378506206645681449475758856053641206175913163492821894709155329556294181613669730336931773953,  # noqa
            key[3].native
        )
        self.assertEqual(
            166647390172913547327716251713919741459272587597255782032652236515036001974461323181989715320980256918783849999012066159723695368018857439366733087649658067943054926668058248612521531843495934099419046629521378187012692776633310821178903471282399402138521150042979117060141563972064613977168440186057796106743,  # noqa
            key[4].native
        )
        self.assertEqual(
            143440533284701431115857974625778819273481773744021067505004499855263691219807413711274106281992493130281690570930126889424222979194828112331057105055939481042398415265558356642606674863401518188395487842736496447305100392269029249928750130190700690239916449523411304928539660679996452045625683879143320460249,  # noqa
            key[5].native
        )
        self.assertEqual(
            109414079859473229289779858629449815451592843305649008118818271892297238643195390011716060554289324731958287404176117228233683079641781234394481865640434212819044363330635799312574408253258259431525735957118503776629524657609514187779529692628749620437591384488141789034909003405007374076072765197764330205487,  # noqa
            key[6].native
        )
        self.assertEqual(
            39361498857013145813625735320048312950154816653378623953034178027634194773898965899927575680536994315500952488328843279054659597751495930118280223039291020752651068863936425009698924893471060669547041417272275998418220630400632040385105243470857091616562513209775072216226822370097138922876120342440353924609,  # noqa
            key[7].native
        )
        self.assertEqual(
            109796662729796355370195012683418958273962986010546166376879205603219777065076464250440708895625560840314914603409569660942497623175203159192440744329997446961447023349392064212216532091513743978251892999757210494211477167363008686808094766092274115601607346901935491774285446659775729268493276413171032997893,  # noqa
            key[8].native
        )

        with self.assertRaises(KeyError):
            key[9].native

    def test_parse_dsa_private_key(self):
        with open(os.path.join(fixtures_dir, 'keys/test-dsa-der.key'), 'rb') as f:
            key = keys.DSAPrivateKey.load(f.read())

        self.assertEqual(
            0,
            key['version'].native
        )
        self.assertEqual(
            4511743893397705393934377497936985478231822206263141826261443300639402520800626925517264115785551703273809312112372693877437137848393530691841757974971843334497076835630893064661599193178307024379015589119302113551197423138934242435710226975119594589912289060014025377813473273600967729027125618396732574594753039493158066887433778053086408525146692226448554390096911703556213619406958876388642882534250747780313634767409586007581976273681005928967585750017105562145167146445061803488570714706090280814293902464230717946651489964409785146803791743658888866280873858000476717727810363942159874283767926511678640730707887895260274767195555813448140889391762755466967436731106514029224490921857229134393798015954890071206959203407845438863870686180087606429828973298318856683615900474921310376145478859687052812749087809700610549251964102790514588562086548577933609968589710807989944739877028770343142449461177732058649962678857,  # noqa
            key['p'].native
        )
        self.assertEqual(
            71587850165936478337655415373676526523562874562337607790945426056266440596923,
            key['q'].native
        )
        self.assertEqual(
            761437146067908309288345767887973163494473925243194806582679580640442238588269326525839153095505341738937595419375068472941615006110237832663093084973431440436421580371384720052414080562019831325744042316268714195397974084616335082272743706567701546951285088540646372701485690904535540223121118329044403681933304838754517522024738251994717369464179515923093116622352823578284891812676662979104509631349201801577889230316128523885862472086364717411346341249139971907827526291913249445756671582283459372536334490171231311487207683108274785825764378203622999309355578169139646003751751448501475767709869676880946562283552431757983801739671783678927397420797147373441051876558068212062253171347849380506793433921881336652424898488378657239798694995315456959568806256079056461448199493507273882763491729787817044805150879660784158902456811649964987582162907020243296662602990514615480712948126671999033658064244112238138589732202,  # noqa
            key['g'].native
        )
        self.assertEqual(
            934231235067929794039535952071098031636053793876274937162425423023735221571983693370780054696865229184537343792766496068557051933738826401423094028670222490622041397241325320965905259541032379046252395145258594355589801644789631904099105867133976990593761395721476198083091062806327384261369876465927159169400428623265291958463077792777155465482611741502621885386691681062128487785344975981628995609792181581218570320181053055516069553767918513262908069925035292416868414952256645902605335068760774106734518308281769128146479819566784704033671969858507248124850451414380441279385481154336362988505436125981975735568289420374790767927084033441728922597082155884801013899630856890463962357814273014111039522903328923758417820349377075487103441305806369234738881875734407495707878637895190993370257589211331043479113328811265005530361001980539377903738453549980082795009589559114091215518866106998956304437954236070776810740036,  # noqa
            key['public_key'].native
        )
        self.assertEqual(
            67419307522580891944110478232775481982040250615628832761657973309422062357004,
            key['private_key'].native
        )

    def test_parse_ec_private_key(self):
        with open(os.path.join(fixtures_dir, 'keys/test-ec-der.key'), 'rb') as f:
            key = keys.ECPrivateKey.load(f.read())

        self.assertEqual(
            'ecPrivkeyVer1',
            key['version'].native
        )
        self.assertEqual(
            105342176757643535635985202437872662036661123763048203788770333621775587689309,
            key['private_key'].native
        )
        self.assertEqual(
            util.OrderedDict([
                ('version', 'ecdpVer1'),
                (
                    'field_id',
                    util.OrderedDict([
                        ('field_type', 'prime_field'),
                        ('parameters', 115792089210356248762697446949407573530086143415290314195533631308867097853951)
                    ])
                ),
                (
                    'curve',
                    util.OrderedDict([
                        (
                            'a',
                            b'\xFF\xFF\xFF\xFF\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'
                            b'\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFC'
                        ),
                        (
                            'b',
                            b'\x5A\xC6\x35\xD8\xAA\x3A\x93\xE7\xB3\xEB\xBD\x55\x76\x98\x86\xBC'
                            b'\x65\x1D\x06\xB0\xCC\x53\xB0\xF6\x3B\xCE\x3C\x3E\x27\xD2\x60\x4B'
                        ),
                        ('seed', b'\xC4\x9D\x36\x08\x86\xE7\x04\x93\x6A\x66\x78\xE1\x13\x9D\x26\xB7\x81\x9F\x7E\x90'),
                    ])
                ),
                (
                    'base',
                    b'\x04\x6B\x17\xD1\xF2\xE1\x2C\x42\x47\xF8\xBC\xE6\xE5\x63\xA4\x40\xF2\x77'
                    b'\x03\x7D\x81\x2D\xEB\x33\xA0\xF4\xA1\x39\x45\xD8\x98\xC2\x96\x4F\xE3\x42'
                    b'\xE2\xFE\x1A\x7F\x9B\x8E\xE7\xEB\x4A\x7C\x0F\x9E\x16\x2B\xCE\x33\x57\x6B'
                    b'\x31\x5E\xCE\xCB\xB6\x40\x68\x37\xBF\x51\xF5'
                ),
                (
                    'order',
                    115792089210356248762697446949407573529996955224135760342422259061068512044369
                ),
                ('cofactor', 1),
                ('hash', None),
            ]),
            key['parameters'].native
        )
        self.assertEqual(
            b'\x04\x8B\x5D\x4C\x71\xF7\xD6\xC6\xA3\x49\x63\x42\x5C\x47\x9F\xCB\x73\x24\x1D\xC9\xDD'
            b'\xD1\x2D\xF1\x3A\x9F\xB7\x04\xDE\x20\xD0\x58\x00\x93\x54\xF6\x89\xC7\x2F\x87\x2B\xF7'
            b'\xF9\x3D\x3B\x34\xED\x9E\x7B\x0E\x3D\x57\x42\xDF\x78\x03\x0B\xCC\x31\xC6\x03\xD7\x9F'
            b'\x60\x01',
            key['public_key'].native
        )

    def test_parse_rsa_public_key(self):
        with open(os.path.join(fixtures_dir, 'keys/test-public-rsa-der.key'), 'rb') as f:
            key = keys.RSAPublicKey.load(f.read())

        self.assertEqual(
            23903990516906431865559598284199534387004799030432486061102966678620221767754702651554142956492614440585611990224871381291841413369032752409360196079700921141819811294444393525264295297988924243231844876926173670633422654261873814968313363171188082579071492839040415373948505938897419917635370450127498164824808630475648771544810334682447182123219422360569466851807131368135806769502898151721274383486320505905826683946456552230958810028663378886363555981449715929872558073101554364803925363048965464124465016494920967179276744892632783712377912841537032383450409486298694116013299423220523450956288827030007092359007,  # noqa
            key['modulus'].native
        )
        self.assertEqual(
            65537,
            key['public_exponent'].native
        )

    def test_parse_public_key_info(self):
        with open(os.path.join(fixtures_dir, 'keys/test-public-der.key'), 'rb') as f:
            key = keys.PublicKeyInfo.load(f.read())

        public_key = key['public_key'].parsed

        self.assertEqual(
            'rsa',
            key['algorithm']['algorithm'].native
        )
        self.assertEqual(
            None,
            key['algorithm']['parameters'].native
        )
        self.assertEqual(
            23903990516906431865559598284199534387004799030432486061102966678620221767754702651554142956492614440585611990224871381291841413369032752409360196079700921141819811294444393525264295297988924243231844876926173670633422654261873814968313363171188082579071492839040415373948505938897419917635370450127498164824808630475648771544810334682447182123219422360569466851807131368135806769502898151721274383486320505905826683946456552230958810028663378886363555981449715929872558073101554364803925363048965464124465016494920967179276744892632783712377912841537032383450409486298694116013299423220523450956288827030007092359007,  # noqa
            public_key['modulus'].native
        )
        self.assertEqual(
            65537,
            public_key['public_exponent'].native
        )

    def test_parse_pkcs8_private_key(self):
        with open(os.path.join(fixtures_dir, 'keys/test-pkcs8-der.key'), 'rb') as f:
            key_info = keys.PrivateKeyInfo.load(f.read())

        key = key_info['private_key'].parsed

        self.assertEqual(
            0,
            key_info['version'].native
        )
        self.assertEqual(
            'rsa',
            key_info['private_key_algorithm']['algorithm'].native
        )
        self.assertEqual(
            None,
            key_info['private_key_algorithm']['parameters'].native
        )

        self.assertEqual(
            'two-prime',
            key['version'].native
        )
        self.assertEqual(
            23903990516906431865559598284199534387004799030432486061102966678620221767754702651554142956492614440585611990224871381291841413369032752409360196079700921141819811294444393525264295297988924243231844876926173670633422654261873814968313363171188082579071492839040415373948505938897419917635370450127498164824808630475648771544810334682447182123219422360569466851807131368135806769502898151721274383486320505905826683946456552230958810028663378886363555981449715929872558073101554364803925363048965464124465016494920967179276744892632783712377912841537032383450409486298694116013299423220523450956288827030007092359007,  # noqa
            key['modulus'].native
        )
        self.assertEqual(
            65537,
            key['public_exponent'].native
        )
        self.assertEqual(
            9979296894007354255484849917690758820642557661666429934720496335307525025035760937280030384204921358841911348590147260206368632524783497961763507098900120579828036636037636859350155169644276779450131617753331883188587268575077705380671279069284616924232052795766448946873233783789819627790465470123569125678598045748629782316184667685110712273519313310937077963014676074966877849272992367512921997850502687035430136911690081438185238817835171119161013656103255853961444458012340770881411877222316871444386486841632394098449378506206645681449475758856053641206175913163492821894709155329556294181613669730336931773953,  # noqa
            key['private_exponent'].native
        )
        self.assertEqual(
            166647390172913547327716251713919741459272587597255782032652236515036001974461323181989715320980256918783849999012066159723695368018857439366733087649658067943054926668058248612521531843495934099419046629521378187012692776633310821178903471282399402138521150042979117060141563972064613977168440186057796106743,  # noqa
            key['prime1'].native
        )
        self.assertEqual(
            143440533284701431115857974625778819273481773744021067505004499855263691219807413711274106281992493130281690570930126889424222979194828112331057105055939481042398415265558356642606674863401518188395487842736496447305100392269029249928750130190700690239916449523411304928539660679996452045625683879143320460249,  # noqa
            key['prime2'].native
        )
        self.assertEqual(
            109414079859473229289779858629449815451592843305649008118818271892297238643195390011716060554289324731958287404176117228233683079641781234394481865640434212819044363330635799312574408253258259431525735957118503776629524657609514187779529692628749620437591384488141789034909003405007374076072765197764330205487,  # noqa
            key['exponent1'].native
        )
        self.assertEqual(
            39361498857013145813625735320048312950154816653378623953034178027634194773898965899927575680536994315500952488328843279054659597751495930118280223039291020752651068863936425009698924893471060669547041417272275998418220630400632040385105243470857091616562513209775072216226822370097138922876120342440353924609,  # noqa
            key['exponent2'].native
        )
        self.assertEqual(
            109796662729796355370195012683418958273962986010546166376879205603219777065076464250440708895625560840314914603409569660942497623175203159192440744329997446961447023349392064212216532091513743978251892999757210494211477167363008686808094766092274115601607346901935491774285446659775729268493276413171032997893,  # noqa
            key['coefficient'].native
        )
        self.assertEqual(
            None,
            key['other_prime_infos'].native
        )

        self.assertEqual(
            None,
            key_info['attributes'].native
        )

    @staticmethod
    def key_sha1_hashes():
        return (
            ('keys/test-public-der.key', b'\xbeB\x85=\xcc\xff\xe3\xf9(\x02\x8f~XV\xb4\xfd\x03\\\xeaK'),
            ('keys/test-public-dsa-der.key', b'\x81\xa37\x86\xf9\x99(\xf2tp`\x87\xf2\xd3~\x8d\x19a\xa8\xbe'),
            ('keys/test-public-ec-named-der.key', b'#\x8d\xee\xeeGH*\xe45T\xb8\xfdVh\x16_\xe2\xaa\xcd\x81'),
            ('keys/test-public-ec-der.key', b'T\xaaTpl4\x1am\xeb]\x97\xd7\x1e\xfc\xd5$<\x8a\x0e\xd7'),
        )

    @data('key_sha1_hashes')
    def sha1(self, relative_path, sha1):
        with open(os.path.join(fixtures_dir, relative_path), 'rb') as f:
            public_key = keys.PublicKeyInfo.load(f.read())

        self.assertEqual(sha1, public_key.sha1)

    @staticmethod
    def key_sha256_hashes():
        return (
            (
                'keys/test-public-der.key',
                b'\xd9\x80\xdf\x94J\x8e\x1e\xf5z\xd2o\x8eS\xa8\x03qX\x9a[\x17g\x12\x89\xc5\xcc\xca\x04\x94\xf2R|F'
            ),
            (
                'keys/test-public-dsa-der.key',
                b'<\x10X\xbf=\xe4\xec3\xb9\xb2 \x11\xce9\xca\xd4\x95\xcf\xf9\xbc\x91q]O\x8f4\xbf\xdb\xdc\xe2\xd6\x82'
            ),
            (
                'keys/test-public-ec-named-der.key',
                b'\x87e \xb4\x13\x8cu\xdd\x11\x92\xa4\xd9;\x8e\xe5"p\xb2\xb7\xa7\xcb8\x88\x16;f\xb9\xf8I\x86J\x1c'
            ),
            (
                'keys/test-public-ec-der.key',
                b'\xf3\xa3k\xe0\xbf\xa9\xd9sl\xaa\x99\xe7\x9c-\xec\xb9\x0e\xe2d\xe9\xc3$\xb9\x893\x99A\xc19ec_'
            ),
        )

    @data('key_sha256_hashes')
    def sha256(self, relative_path, sha256):
        with open(os.path.join(fixtures_dir, relative_path), 'rb') as f:
            public_key = keys.PublicKeyInfo.load(f.read())

        self.assertEqual(sha256, public_key.sha256)

    @staticmethod
    def key_pairs():
        return (
            (
                'dsa',
                'keys/test-pkcs8-dsa-der.key',
                'keys/test-public-dsa-der.key',
                'dsa',
                3072
            ),
            (
                'ec_named',
                'keys/test-pkcs8-ec-named-der.key',
                'keys/test-public-ec-named-der.key',
                'ec',
                256
            ),
            (
                'ec',
                'keys/test-pkcs8-ec-der.key',
                'keys/test-public-ec-der.key',
                'ec',
                256
            ),
            (
                'rsa',
                'keys/test-pkcs8-der.key',
                'keys/test-public-der.key',
                'rsa',
                2048
            ),
        )

    @data('key_pairs', True)
    def algorithm_name(self, private_key_file, public_key_file, algorithm, _):
        with open(os.path.join(fixtures_dir, private_key_file), 'rb') as f:
            private_key = keys.PrivateKeyInfo.load(f.read())
        with open(os.path.join(fixtures_dir, public_key_file), 'rb') as f:
            public_key = keys.PublicKeyInfo.load(f.read())

        self.assertEqual(algorithm, private_key.algorithm)
        self.assertEqual(algorithm, public_key.algorithm)

    @data('key_pairs', True)
    def bit_size(self, private_key_file, public_key_file, _, bit_size):
        with open(os.path.join(fixtures_dir, private_key_file), 'rb') as f:
            private_key = keys.PrivateKeyInfo.load(f.read())
        with open(os.path.join(fixtures_dir, public_key_file), 'rb') as f:
            public_key = keys.PublicKeyInfo.load(f.read())

        self.assertEqual(bit_size, private_key.bit_size)
        self.assertEqual(bit_size, public_key.bit_size)

    @staticmethod
    def key_variations():
        return (
            (
                'dsa',
                'keys/test-pkcs8-dsa-der.key',
                'keys/test-dsa-der.key',
            ),
            (
                'ec_named',
                'keys/test-pkcs8-ec-named-der.key',
                'keys/test-ec-named-der.key',
            ),
            (
                'ec',
                'keys/test-pkcs8-ec-der.key',
                'keys/test-ec-der.key',
            ),
            (
                'rsa',
                'keys/test-pkcs8-der.key',
                'keys/test-der.key',
            ),
        )

    def test_curve_invalid(self):
        with open(os.path.join(fixtures_dir, 'keys/test-pkcs8-der.key'), 'rb') as f:
            private_key = keys.PrivateKeyInfo.load(f.read())

        with self.assertRaises(ValueError):
            private_key.curve

        with open(os.path.join(fixtures_dir, 'keys/test-public-rsa-der.key'), 'rb') as f:
            public_key = keys.PublicKeyInfo.load(f.read())

        with self.assertRaises(ValueError):
            public_key.curve

    def test_curve_info_name(self):
        with open(os.path.join(fixtures_dir, 'keys/test-pkcs8-ec-named-der.key'), 'rb') as f:
            private_key = keys.PrivateKeyInfo.load(f.read())

        curve = ('named', 'secp256r1')

        self.assertEqual(curve, private_key.curve)

        with open(os.path.join(fixtures_dir, 'keys/test-public-ec-named-der.key'), 'rb') as f:
            public_key = keys.PublicKeyInfo.load(f.read())

        self.assertEqual(curve, public_key.curve)

    def test_curve_info_specified(self):
        with open(os.path.join(fixtures_dir, 'keys/test-pkcs8-ec-der.key'), 'rb') as f:
            private_key = keys.PrivateKeyInfo.load(f.read())

        curve = (
            'specified',
            util.OrderedDict([
                ('version', 'ecdpVer1'),
                (
                    'field_id',
                    util.OrderedDict([
                        ('field_type', 'prime_field'),
                        ('parameters', 115792089210356248762697446949407573530086143415290314195533631308867097853951)
                    ])
                ),
                (
                    'curve',
                    util.OrderedDict([
                        (
                            'a',
                            b'\xFF\xFF\xFF\xFF\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'
                            b'\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFC'
                        ),
                        (
                            'b',
                            b'\x5A\xC6\x35\xD8\xAA\x3A\x93\xE7\xB3\xEB\xBD\x55\x76\x98\x86\xBC'
                            b'\x65\x1D\x06\xB0\xCC\x53\xB0\xF6\x3B\xCE\x3C\x3E\x27\xD2\x60\x4B'
                        ),
                        (
                            'seed',
                            b'\xC4\x9D\x36\x08\x86\xE7\x04\x93\x6A\x66\x78\xE1\x13\x9D\x26\xB7\x81\x9F\x7E\x90'
                        ),
                    ])
                ),
                (
                    'base',
                    b'\x04\x6B\x17\xD1\xF2\xE1\x2C\x42\x47\xF8\xBC\xE6\xE5\x63\xA4\x40\xF2\x77\x03\x7D'
                    b'\x81\x2D\xEB\x33\xA0\xF4\xA1\x39\x45\xD8\x98\xC2\x96\x4F\xE3\x42\xE2\xFE\x1A\x7F'
                    b'\x9B\x8E\xE7\xEB\x4A\x7C\x0F\x9E\x16\x2B\xCE\x33\x57\x6B\x31\x5E\xCE\xCB\xB6\x40'
                    b'\x68\x37\xBF\x51\xF5'
                ),
                (
                    'order',
                    115792089210356248762697446949407573529996955224135760342422259061068512044369
                ),
                ('cofactor', 1),
                ('hash', None),
            ])
        )

        self.assertEqual(curve, private_key.curve)

        with open(os.path.join(fixtures_dir, 'keys/test-public-ec-der.key'), 'rb') as f:
            public_key = keys.PublicKeyInfo.load(f.read())

        self.assertEqual(curve, public_key.curve)

    def test_named_curve_register(self):
        keys.NamedCurve.register('customcurve', '1.2.3.4.5.6.7.8', 16)

        k = keys.NamedCurve('customcurve')
        self.assertEqual('customcurve', k.native)
        self.assertEqual('1.2.3.4.5.6.7.8', k.dotted)

        k = keys.ECPrivateKey({
            'version': 1,
            'private_key': 1,
            'parameters': keys.ECDomainParameters(('named', 'customcurve')),
        })

        self.assertEqual('ecPrivkeyVer1', k['version'].native)
        self.assertEqual(1, k['private_key'].native)
        self.assertEqual('customcurve', k['parameters'].native)
        self.assertEqual(
            b'\x04\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01',
            k['private_key'].dump()
        )

    def test_ec_private_key_width(self):
        k = keys.ECPrivateKey({
            'version': 1,
            'private_key': 1,
            'parameters': keys.ECDomainParameters(('named', 'secp256r1')),
        })

        self.assertEqual('ecPrivkeyVer1', k['version'].native)
        self.assertEqual(1, k['private_key'].native)
        self.assertEqual('secp256r1', k['parameters'].native)
        self.assertEqual(
            b'\x04\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01',
            k['private_key'].dump()
        )

    def test_ec_private_key_width_dotted(self):
        k = keys.ECPrivateKey({
            'version': 1,
            'private_key': 1,
            'parameters': keys.ECDomainParameters(('named', '1.3.132.0.10')),
        })

        self.assertEqual('ecPrivkeyVer1', k['version'].native)
        self.assertEqual(1, k['private_key'].native)
        self.assertEqual('secp256k1', k['parameters'].native)
        self.assertEqual(
            b'\x04\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01',
            k['private_key'].dump()
        )

    def test_ec_private_key_info_width(self):
        pki = keys.PrivateKeyInfo({
            'version': 0,
            'private_key_algorithm': {
                'algorithm': 'ec',
                'parameters': ('named', 'secp256r1'),
            },
            'private_key': {
                'version': 1,
                'private_key': 1
            }
        })

        k = pki['private_key'].parsed
        self.assertEqual('ecPrivkeyVer1', k['version'].native)
        self.assertEqual(1, k['private_key'].native)
        self.assertEqual(None, k['parameters'].native)
        self.assertEqual(
            b'\x04\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01',
            k['private_key'].dump()
        )
