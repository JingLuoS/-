---
title: "-----------------����ϵͳģ���¼����ȡ�α�------------------"
output: html_document
---

## ��¼���̼�Ҫ˵��

>### ע��
>* *httpЭ������״̬�ģ�Ҳ����˵һ�����ӹ������������ס��һ�ε�������Ϊ�������е�¼���ڵ�½���к�����������Ϊ������ʹ��������һ����Ϊ��ס���ǵĵ�½״̬.��cookies,�ɷ��������ɱ����ڿͻ��ˡ�*
>* *��python��requests���http��������˷�װ���ṩ�˶���Ϣ�Ĵ�����������cookies������session�Ự���������Զ����棬���ö����ȡcookies��һ��session��һϵ�������Ĳ�����*
>* *׼���������ݰ�����������ʹ��������Դ������߹���*
>* *����������python3*
>### ����˵��
> 1. ��ȡcsrftoken
>>* token�ڵ�¼ҳ��ǰ����js����
>>* ��http://jwgl8.ujn.edu.cn/jwglxt/xtgl/login_slogin.html?language=zh_CN����get���󣬻�ȡ���ص�htmlҳ��
>>* pythin������ʽ��ȡhtml�����е�csrftoken��valueֵ

> 2. ��ȡexponent��modulus���ɹ�Կ
>>* ��http://jwgl8.ujn.edu.cn/jwglxt/xtgl/login_getPublicKey.html?time=...."����get����
>>* ע�����������Ҫ����ʱ�����ԭ��ҳʹ��js���ɵ�13λʱ���������python��ֻ�ܾ�ȷ���뼴10λ����ʵ����10λ������������������λ������Ҳ����ֱ�ӳ���1000��
>>* ���ܵ���exponent��modulusΪbase64������ַ����������������publicKey(�����˵�����崦��)�������㷨����rsa��

> 3. ��ȡ��¼״̬������¼�ɹ���״̬���浽session
>>* ��http://jwgl8.ujn.edu.cn/jwglxt/xtgl/login_slogin.html����post����
>>* post��Я������

                data = {
                        "csrftoken":
                        "yhm":�û���
                        "mm":����(���ܺ�)
                        "mm":����(���ܺ�)
                         }

>>* fiddlerץȡ���ݰ�����headers��Ϊ�˴���������ͷ

> 4. ��ȡ�α�
>>* ��http://jwgl8.ujn.edu.cn/jwglxt/kbcx/xskbcx_cxXsKb.html?gnmkdm=N2151����post����

                data = {
                    "xnm":ѧ��
                    "xqm":ѧ�ڣ���һ��ڶ�ѧ��         
                    }
>>* ��ȡ���ص�json���ݣ�����ȡ���������

## ����API

> 1. Class GetLogin:
>>* __init__(self, username, passward)------//��ʼ��
>>* getCsrftoken()    ------//��ȡtoken
>>* getPublicKeyAndEncrypt() ------//��ȡexponent��modulus������PublicKeyȻ���������
>>* getLogin()------//��ȡ��¼״̬

> 2. Class GetInfo(GetLogin):
>>* __init__(self,username,password,school_year,semester)------//�̳�GetLOgin����Ҫ�õ�GetLogin���session�Ự
>>* getCourse()------//��ȡ�α���������

> 3. Class Connection(GetInfo):
>>* __init__(self,username,password,school_year,semester)------//�̳�GetInfo����Ҫ�õ�GetInfo����session�Ự��getCourse
>>* formatData()------//��ʽ��������������
>>* isExistUserCourse()------//������ݿ��Ƿ��б��ݣ�����ֱ��ȡ����û�������getCourse,���������ݿ�
>>* courseHandle()------//�������Ŀα����ݲ��뵽���ݿ�
>>* getCourseFromMysql------//()�����ݿ��ȡ���ϼ������������

> 4. Class RSAKey:
>>* setPublic(self, N, E)------//��exponent��modulus��hexתΪʮ���� 
>>* encrypt(self, text)------//�������룬��������ܺ�����

## start.py ����
>* ��start.py�ļ�

## exponent��modulus�����Լ�����˵����
>* ԭʼΪbase64�ַ���
>* python��base64����base64���룬���������ַ���ת����hex(��binascii�����)���˲���Ҳ�����б�����ɡ�
>* ��ʮ�����Ƶ�exponent��modulus����publicKey,����֮�����
>* ���ܲ���rsa�㷨������ʮ���������ġ�
>* ��ʮ�����Ƶ����Ĵ������תΪbase64������Ϊpost����Ĳ���

## ��ע
>* mysql���ݿ�v8.0 
>* ���ݿ���course ����school_timetable
>* ���ֶ���
>>* username:ѧ��ѧ��
>>* course_name���γ�����
>>* week������
>>* time��ʱ�䣨������
>>* teacher_name���ڿν�ʦ
>>* address���ص�
>>* which_week����˫��
>>* school_year��ѧ��
>>* semester��ѧ��

    

    

