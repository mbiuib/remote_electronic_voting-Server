import copy
import math
import string
from random import choice

import rsa
from sympy import isprime, randprime


def is_prime(num: int) -> bool:
    """Проверка числа на простоту.

    :param int num: проверяемое число.
    :return: ``True`` или ``False``.
    :rtype: bool

    :example:
    >>> is_prime(65537)
    True
    >>> is_prime(65538)
    False
    """

    return isprime(num)


def gcd_and_simpl(n: int) -> int:
    """Возвращает случайное простое число, взаимнопростое с аргументом.

    :param int n: число для проверки.
    :return: случайное простое число взаимнопростое с проверяемым.
    :rtype: int

    :example:
    >>> gcd_and_simpl(65537)
    16187
    >>> gcd_and_simpl(65537)
    5693
    """

    while True:
        rand_prime = randprime(1, n)
        if math.gcd(n, rand_prime):
            return rand_prime


def mask(int_msg: int, masking_factor: int, e: int, n: int) -> int:
    """Маскирование числа алгоритмом RSA. Поддерживается маскирование
    очень больших простых чисел.

    :param int int_msg: сообщение для маскирования, представленное списком кодов.
    :param int masking_factor: число, взаимнопростое с параметром n,
        обычно известно только стороне, производящей маскирование.
    :param int e: открытая экспонента, первая часть открытого ключа RSA.
    :param int n: простое число, вторая часть открытого ключа RSA.
    :return: замаскированное число
    :rtype: int

    :example:
    >>> mask(9022753473110032654548339973537471249745533337660269233170935060939627132412694558764787596245010015, 4820796477759748212320947648627878599674576581140590630080674200955582700417083207928026201225144906464627316516100108323384746856098440784965076183617593930381477211755764865109478871039414052239318789091220955972131791530554490882740721237293569697737039829602141178821956353264171225049944012399926431725592943407679976639469930603880840867603043794066141454252582438402722793583685564137514406037871630301251276811311732755553143251606157780326911822293553389410004401815793119738582203624217184602658419288626384324702602055116810748611206001415701006657524871016257593112339282507001245945867216515354833153657, 65537, 20361876765348507325602180832898758614575054677416140431428695025549032856211077332119381668579250277218278402025167356310121137583206160686182747663633712449905863242437197033937673823484252324516182455542321440174215024880354559373008047389342960057248086689157265113806187970243110089605097167787460021819357974682607960418568785018619989167988503115581001038648425798539386924645777653042278375147473705936994994748817866602721130466852599578126797951601013908200937188252070277119235915607769026357112934647366009495451075694118368468105015471392731769146965806550414217525721522795589505817885739040029849413419)
    15804088622747537301875565728207539776273377157425810978093837786966335723601915960255638517505727709894733882204357257130559608543968191817629193774004996110066652756853462892227262007219418801091566381919388381257450621255278408795628137952274007990108747700383069936154014046337036129790803362207900142248225918254278942696843952812478948709309412617290576850997355012598812053944646050707955564852281896237449187981507010032225464639149571499905312365781683711239401487152704111639495680244408938561808856383855181151174128384098250662632445014745528556726039491062173710639287709103689143586876095991737589071342
    """

    int_msg_ = copy.deepcopy(int_msg)
    return pow(int_msg_ * pow(masking_factor, e, n), 1, n)


def demask(int_msg: int, masking_factor: int, n: int) -> int:
    """Демаскирование числа алгоритмом RSA. Поддерживается демаскирование
    очень больших простых чисел.

    :param int int_msg: Сообщение для демаскирования, представленное списком чисел.
    :param int masking_factor: Число, взаимнопростое с параметром n,
        обычно известно только стороне, производящей маскирование.
    :param int n: Простое число, часть открытого ключа RSA.
    :return: список демаскированных кодов.
    :rtype: int

    :example:
    >>> demask(16392736375062917048868290050008110139611007410802462267452084318517473758790770226690650160104349963275451780523119335468622704793627374168782073909861401249255428698620500118932861049006270201091011404730126916619803258772679777719723045396422735334494602493042536660506349278074923599262718669426862961658453312158780601698906623298632398673582558062559742315821567624709206728742607149587439176343951859392176161152067283680233051429321806704565585162168563713847477977267018847403886166583262891863345518310913949425300645011723853122408338116335331373479093380639430001003827750626489036154909365753924283571409, 4820796477759748212320947648627878599674576581140590630080674200955582700417083207928026201225144906464627316516100108323384746856098440784965076183617593930381477211755764865109478871039414052239318789091220955972131791530554490882740721237293569697737039829602141178821956353264171225049944012399926431725592943407679976639469930603880840867603043794066141454252582438402722793583685564137514406037871630301251276811311732755553143251606157780326911822293553389410004401815793119738582203624217184602658419288626384324702602055116810748611206001415701006657524871016257593112339282507001245945867216515354833153657, 20361876765348507325602180832898758614575054677416140431428695025549032856211077332119381668579250277218278402025167356310121137583206160686182747663633712449905863242437197033937673823484252324516182455542321440174215024880354559373008047389342960057248086689157265113806187970243110089605097167787460021819357974682607960418568785018619989167988503115581001038648425798539386924645777653042278375147473705936994994748817866602721130466852599578126797951601013908200937188252070277119235915607769026357112934647366009495451075694118368468105015471392731769146965806550414217525721522795589505817885739040029849413419)
    8931535887828620156093874273919057257065334579009478491419645781554454173379404847347250616829916883341532146794735904568424195437155596713962746571029627579205642926456129577861116718656997743835285679942786648660788718289232486463249114928340976648150678252820947757025499227953441661424691513241288673666245016761646523750117134875916481932207101256213265644863842177177938538950583001157247131072668658595153481647691256716177687415062225555340342840539934174535598264955459513474189957162392806559017023148456489739391134676304720545885142272417661176013894892811807819827225113560426258391199052993426309937885
    """

    int_msg_ = copy.deepcopy(int_msg)
    m_ = pow(masking_factor, -1, n)
    return pow(int_msg_ * m_, 1, n)


def sign(int_msg: int, d: int, n: int) -> int:
    """Криптографическая подпись числа алгоритмом RSA. Поддерживаются
    очень большие простые чисела.

    :param int int_msg: сообщение для подписи, представленное списком кодов.
    :param int d: закрытая экспонента, часть закрытого ключа RSA.
    :param int n: простое число, вторая часть открытого ключа RSA.
    :return: подписанное число.
    :rtype: int

    :example:
    >>> sign(15804088622747537301875565728207539776273377157425810978093837786966335723601915960255638517505727709894733882204357257130559608543968191817629193774004996110066652756853462892227262007219418801091566381919388381257450621255278408795628137952274007990108747700383069936154014046337036129790803362207900142248225918254278942696843952812478948709309412617290576850997355012598812053944646050707955564852281896237449187981507010032225464639149571499905312365781683711239401487152704111639495680244408938561808856383855181151174128384098250662632445014745528556726039491062173710639287709103689143586876095991737589071342, 3619438456289402748541023454263499614497922814937852041417256689689501407329741752514059760461681911561304415410423633714475481058564763209803162974948255818323001647300260027905324042731108385872618200848824250551064389127346168231172536946740383143386271035552121900171997469495279129005290183003914562823224188353015598710672878656460021605264863474179243624287871813900258254469652042189360008181223414514383156080575105273626565289421570800181157347704698165398358510023750872813361292910242599551154205422782439236020550013988805255176517140487876113136261729628302157480000709284635595944960810665516608321985, 22799609583798403299801331614962223590479658546960977435444324459071593015394971668061700742154675839868628169238075132905188350839596202083897529016645890192756109088727137778626607246104253199243923397638350144979345143237109364414297823325502161675135144642154883984195713010218387954407110486011267922969907269671004854752852862184468635614905803430360508382983594772890108723039191868203285469900605180577466383319757888074558731870616314693752657355351610333881966979549618337747754273147578504764514771211127092490762724563969848183224852749560739477729888711234601336818238478511053648217080102754495130029327)
    17065352469390105566237944952105900422813971440201416478943294358189889263900067403531010961580978652888524501564364361642144939761871320574358835920624316129170321242293876916686072334064104925031580579894320473917348608382874786364604898211341430621549948227651846840937905833367508681241445728424758905535742189445082910931339648813931014002780108316989089125167514424444173584689623169332371154619642073649697240215831745338342223998234836852484095631227152944657194049540305144857503914633541871947186685364839892816018590863281073478937823023814913160754414817824342971994667033892694698272305580407224236369120
    """

    return pow(int_msg, d, n)


def sign_list(int_msg: list[int], d: int, n: int) -> list[int]:
    """Криптографическая подпись списка чисел алгоритмом RSA. Поддерживаются
        очень большие простые чисела. Используется, как обертка над функцией
        :py:func:`sign()`

        :param list[int] int_msg: сообщение для подписи, представленное списком кодов.
        :param int d: закрытая экспонента, часть закрытого ключа RSA.
        :param int n: простое число, вторая часть открытого ключа RSA.
        :return: список подписанных чисел.
        :rtype: list[int]
    """
    return [sign(i, d, n) for i in int_msg]


def unsign(int_msg: int, e: int, n: int) -> int:
    """Снимает криптографическую подпись RSA. Поддерживаются очень большие простые чисела

    :param int int_msg: сообщение для снятия подписи, представленное списком кодов.
    :param int e: открытая экспонента, первая часть открытого ключа RSA.
    :param int n: простое число, вторая часть открытого ключа RSA.
    :return: число со снятой подписью.
    :rtype: int

    :example:
    >>> unsign(17065352469390105566237944952105900422813971440201416478943294358189889263900067403531010961580978652888524501564364361642144939761871320574358835920624316129170321242293876916686072334064104925031580579894320473917348608382874786364604898211341430621549948227651846840937905833367508681241445728424758905535742189445082910931339648813931014002780108316989089125167514424444173584689623169332371154619642073649697240215831745338342223998234836852484095631227152944657194049540305144857503914633541871947186685364839892816018590863281073478937823023814913160754414817824342971994667033892694698272305580407224236369120,65537,22799609583798403299801331614962223590479658546960977435444324459071593015394971668061700742154675839868628169238075132905188350839596202083897529016645890192756109088727137778626607246104253199243923397638350144979345143237109364414297823325502161675135144642154883984195713010218387954407110486011267922969907269671004854752852862184468635614905803430360508382983594772890108723039191868203285469900605180577466383319757888074558731870616314693752657355351610333881966979549618337747754273147578504764514771211127092490762724563969848183224852749560739477729888711234601336818238478511053648217080102754495130029327)
    15804088622747537301875565728207539776273377157425810978093837786966335723601915960255638517505727709894733882204357257130559608543968191817629193774004996110066652756853462892227262007219418801091566381919388381257450621255278408795628137952274007990108747700383069936154014046337036129790803362207900142248225918254278942696843952812478948709309412617290576850997355012598812053944646050707955564852281896237449187981507010032225464639149571499905312365781683711239401487152704111639495680244408938561808856383855181151174128384098250662632445014745528556726039491062173710639287709103689143586876095991737589071342
    """
    return pow(int_msg, e, n)


def unsign_list(int_msg: list[int], e: int, n: int) -> list[int]:
    """Снятие криптографической подписи списка чисел алгоритмом RSA. Поддерживаются
    очень большие простые чисела. Используется, как обертка над функцией
    :py:func:`unsign()`

    :param list[int] int_msg: сообщение для подписи, представленное списком кодов.
    :param int e: закрытая экспонента, часть закрытого ключа RSA.
    :param int n: простое число, вторая часть открытого ключа RSA.
    :return: список чисел со снятой подписью.
    :rtype: list[int]
    """
    return [unsign(i, e, n) for i in int_msg]


def generate_iden_num(l: int) -> int:
    """Генерирует число заданной длины.

    :param l: длина необходимого числа.
    :return: сгенерированное число.
    :rtype: int
    """
    letters = string.digits
    return int(''.join(choice(letters) for _ in range(l)))


def pack_I_n_id(I, n_id) -> int:
    postfix = ("0"*20 + str(n_id))[-20:]
    E_I_n_id = str(I) + postfix
    return int(E_I_n_id)


def unpack_I_n_id(E_I_n_id):
    I = int(str(E_I_n_id)[:-20])
    n_id = int(str(E_I_n_id)[-20:])
    return I, n_id


if __name__ == '__main__':
    # Generate RSA keys
    izb_public_key, izb_private_key = rsa.newkeys(512)
    b_izb_public_key, b_izb_private_key = rsa.newkeys(1024)
    ik_public_key, ik_private_key = rsa.newkeys(512)

    m = gcd_and_simpl(ik_public_key.n)
    I = generate_iden_num(100)
    print("I:", I)
    print("m:", m)

    I_m = mask(I, m, ik_public_key.e, ik_public_key.n)  # client
    q = pack_I_n_id(I_m, 15)
    M_1 = sign(q, b_izb_private_key.d, b_izb_private_key.n)  # client

    M_1_check = unsign(M_1, b_izb_public_key.e, b_izb_public_key.n)
    masked_iden_num, n_id = unpack_I_n_id(M_1_check)
    # n_id, masked_iden_num = M_1_check[1], M_1_check[0]
    I_sm = sign(masked_iden_num, ik_private_key.d, ik_private_key.n)

    I_s = demask(I_sm, m, ik_public_key.n)
    encode_msg = unsign(I_s, ik_public_key.e, ik_public_key.n)

    print(f"I_m: {I_m}")
    print(f"q: {q}")
    print(f"M_1: {M_1}")
    print()

    print(f"n_id: {n_id}")
    print(f"M_1_check: {M_1_check}")
    print(f"I_sm: {I_sm}")
    print()

    print(f"demasked: {I_s}")
    print(f"msg: {encode_msg}")
    print(f"msg check: {encode_msg == I}")
