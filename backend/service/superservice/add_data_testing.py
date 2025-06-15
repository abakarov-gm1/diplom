# для добавления заявки
xml = '''
<ApplicationList>
  <Application>
    <IdObject>1</IdObject>
    
    <EntrantChoice>
      <IdEntrant>1001</IdEntrant>  # тут вместо id использую добавление 
    </EntrantChoice>
    
    <EntrantChoice>
        <AddEntrant>
            <Identification>
                <LastName>Иванов</LastName>
                <FirstName>Иван</FirstName>
                <MiddleName>Иванович</MiddleName>
                <Gender>1</Gender>
                <BirthDate>2005-05-01</BirthDate>
                <IdCitizenship>643</IdCitizenship>
                <Snils>123-456-789 00</Snils>
                <Document>
                    <IdDocumentType>1</IdDocumentType>
                    <DocumentSeries>1234</DocumentSeries>
                    <DocumentNumber>567890</DocumentNumber>
                    <DocumentDate>2020-06-01</DocumentDate>
                    <DocumentOrganization>УФМС России</DocumentOrganization>
                </Document>
            </Identification>
        </AddEntrant>
    </EntrantChoice>
    
    <ApplicationNumber>APP-0001</ApplicationNumber>
    <ApplicationDate>2025-06-11</ApplicationDate>
    <IdStageAdmission>1</IdStageAdmission>
    <IdEducationLevelGroup>1</IdEducationLevelGroup>
    <IdCampaign>1829139</IdCampaign>
    <IdEducationForm>1</IdEducationForm>
    <IdSourceFinancingType>1</IdSourceFinancingType>
    <IsBudget>true</IsBudget>
    <IdCompetition>275761</IdCompetition>
    <FirstHigherEducation>false</FirstHigherEducation>
    <NeedHostel>false</NeedHostel>
    <AllowedForEpgu>true</AllowedForEpgu>
  </Application>
</ApplicationList>
'''




# t = '''
# <ApplicationList>
#   <Application>
#     <IdObject>1</IdObject> <!-- Уникальный идентификатор объекта внутри запроса -->
#
#     <EntrantChoice> <!-- Поступающий -->
#       <IdEntrant>1001</IdEntrant> <!-- ID профиля поступающего -->
#     </EntrantChoice>
#
#     <ApplicationNumber>APP-0001</ApplicationNumber> <!-- Номер заявления -->
#     <ApplicationDate>2025-06-11</ApplicationDate> <!-- Дата подачи заявления -->
#     <IdStageAdmission>1</IdStageAdmission> <!-- Этап приема (из справочника StagesAdmissionCls) --> 1 основной набор или доп 4 id
#     <IdEducationLevelGroup>3</IdEducationLevelGroup> <!-- Уровень образования (справочник EducationLevelGroupCls) --> 1 2 3 - базовые специалитет аспирантура
#     <IdCampaign>4</IdCampaign> <!-- Кампания приема (CampaignList) --> 1829139 это  приемная кампания
#     <IdEducationForm>1</IdEducationForm> <!-- Форма обучения (справочник EducationFormCls) --> очно заочно и тд
#     # <IdSourceFinancingType>1</IdSourceFinancingType> <!-- Источник финансирования (справочник FinancingSourceTypeCls) -->
#     <IsBudget>true</IsBudget> <!-- Бюджет или платно -->
#     <IdCompetition>5</IdCompetition> <!-- Конкурсная группа (из CompetitiveGroupList) --> 275761
#
#     <FirstHigherEducation>false</FirstHigherEducation> <!-- Первое высшее образование -->
#     <NeedHostel>false</NeedHostel> <!-- Требуется общежитие -->
#     <AllowedForEpgu>true</AllowedForEpgu> <!-- Разрешение для ЕПГУ -->
#   </Application>
# </ApplicationList>
# '''



work_final = ''' 
<?xml version="1.0" encoding="utf-8"?>
<!-- Created with Liquid Technologies Online Tools 1.0 (https://www.liquid-technologies.com) -->
<PackageData xsi:noNamespaceSchemaLocation="schema.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <ApplicationList>
    <Application>
      <IdObject>4098</IdObject>
      <EntrantChoice>
        <AddEntrant>
          <Identification>
            <IdDocumentType>100001</IdDocumentType>  // паспорт DocumentTypeCls  вот тут возможно ошибка 
            <DocName>Паспорт гражданина Российской Федерации</DocName>  // выташил оттуда же 
            <DocSeries>8220</DocSeries>
            <DocNumber>665461</DocNumber>
            <DocOrganization>УФМС России</DocOrganization>
            <IssueDate>2011-11-02</IssueDate>
          </Identification>
          <IdGender>1</IdGender>
          <Birthday>2000-04-20</Birthday>
          <Birthplace>Mahachkala</Birthplace>
          <IdOksm>185</IdOksm>
          <AddressList>
            <Address>
              <IsRegistration>true</IsRegistration>
              <FullAddr>Mahachkala</FullAddr>
              <IdRegion>5</IdRegion>
              <City>izberg</City>
            </Address>
          </AddressList>
        </AddEntrant>
      </EntrantChoice>
      <RegistrationDate>1987-08-20T00:47:07.81</RegistrationDate>
      <FirstHigherEducation>true</FirstHigherEducation>
      <NeedHostel>true</NeedHostel>
      <AllowedForEpgu>true</AllowedForEpgu>
      <IdStageAdmission>1</IdStageAdmission> // основной набор / доп набор 4
      <IsBudget>true</IsBudget>
      <IdEducationLevelGroup>1</IdEducationLevelGroup>
      <ExtraTestAttribute>false</ExtraTestAttribute>
      <AddCompetitiveGroupList>
        <AddCompetitiveGroup>
          <IdCompetition>268943</IdCompetition>
          <IdStatus>1</IdStatus>
          <Priority>
            <PriorityTarget>112</PriorityTarget>
          </Priority>
        </AddCompetitiveGroup>
      </AddCompetitiveGroupList>
      <SpecialConditionList>
        <Id>2860</Id>
        <Id>1279</Id>
        <Id>6278</Id>
        <Id>2768</Id>
        <Id>9280</Id>
      </SpecialConditionList>
    </Application>
    
    <Application>
      <IdObject>2286</IdObject>
      <EntrantChoice>
        <AddEntrant>
          <Identification>
            <IdDocumentType>6534</IdDocumentType>
            <DocName>string</DocName>
            <IssueDate>1994-02-04</IssueDate>
          </Identification>
          <IdGender>4358</IdGender>
          <Birthday>1979-07-14</Birthday>
          <Birthplace>string</Birthplace>
          <IdOksm>9941</IdOksm>
          <AddressList>
            <Address>
              <IsRegistration>1</IsRegistration>
              <FullAddr>string</FullAddr>
              <IdRegion>6978</IdRegion>
              <City>string</City>
            </Address>
          </AddressList>
        </AddEntrant>
      </EntrantChoice>
      <RegistrationDate>2018-11-21T04:31:54.05</RegistrationDate>
      <FirstHigherEducation>false</FirstHigherEducation>
      <NeedHostel>1</NeedHostel>
      <AllowedForEpgu>true</AllowedForEpgu>
      <IdStageAdmission>1084</IdStageAdmission>
      <IsBudget>1</IsBudget>
      <IdEducationLevelGroup>447</IdEducationLevelGroup>
      <ExtraTestAttribute>0</ExtraTestAttribute>
      <AddCompetitiveGroupList>
        <AddCompetitiveGroup>
          <IdCompetition>8657</IdCompetition>
          <IdStatus>835</IdStatus>
          <Priority>
            <PriorityTarget>50</PriorityTarget>
          </Priority>
        </AddCompetitiveGroup>
        <AddCompetitiveGroup>
          <IdCompetition>9373</IdCompetition>
          <IdStatus>414</IdStatus>
          <Priority>
            <PriorityTarget>234</PriorityTarget>
          </Priority>
        </AddCompetitiveGroup>
      </AddCompetitiveGroupList>
      <SpecialConditionList>
        <Id>6071</Id>
        <Id>6531</Id>
      </SpecialConditionList>
      <IdDictionaryValueMusic>9494</IdDictionaryValueMusic>
    </Application>
    
    
    <Application>
      <IdObject>9392</IdObject>
      <EntrantChoice>
        <IdEntrant>3648</IdEntrant>
      </EntrantChoice>
      <RegistrationDate>1983-04-10T07:58:51.15</RegistrationDate>
      <FirstHigherEducation>true</FirstHigherEducation>
      <NeedHostel>true</NeedHostel>
      <AllowedForEpgu>true</AllowedForEpgu>
      <IdStageAdmission>4696</IdStageAdmission>
      <IsBudget>1</IsBudget>
      <IdEducationLevelGroup>97</IdEducationLevelGroup>
      <ExtraTestAttribute>0</ExtraTestAttribute>
      <AddCompetitiveGroupList>
        <AddCompetitiveGroup>
          <IdCompetition>9777</IdCompetition>
          <IdStatus>6760</IdStatus>
          <Priority>
            <PriorityOther></PriorityOther>
          </Priority>
        </AddCompetitiveGroup>
        <AddCompetitiveGroup>
          <IdCompetition>8676</IdCompetition>
          <IdStatus>574</IdStatus>
          <Priority>
            <PriorityTarget>93</PriorityTarget>
          </Priority>
        </AddCompetitiveGroup>
      </AddCompetitiveGroupList>
      <IdDictionaryValueMusic>7381</IdDictionaryValueMusic>
    </Application>
    
    
    <Application>
      <IdObject>8571</IdObject>
      <EntrantChoice>
        <IdEntrant>989</IdEntrant>
      </EntrantChoice>
      <RegistrationDate>2009-01-13T00:42:13.57</RegistrationDate>
      <FirstHigherEducation>0</FirstHigherEducation>
      <NeedHostel>0</NeedHostel>
      <AllowedForEpgu>false</AllowedForEpgu>
      <IdStageAdmission>3641</IdStageAdmission>
      <IsBudget>0</IsBudget>
      <IdEducationLevelGroup>6788</IdEducationLevelGroup>
      <ExtraTestAttribute>true</ExtraTestAttribute>
      <AddCompetitiveGroupList>
        <AddCompetitiveGroup>
          <IdCompetition>7981</IdCompetition>
          <IdStatus>8530</IdStatus>
          <Priority>
            <PriorityOther>101</PriorityOther>
          </Priority>
        </AddCompetitiveGroup>
        <AddCompetitiveGroup>
          <IdCompetition>6297</IdCompetition>
          <IdStatus>906</IdStatus>
          <Priority>
            <PriorityTarget>236</PriorityTarget>
          </Priority>
        </AddCompetitiveGroup>
        <AddCompetitiveGroup>
          <IdCompetition>8797</IdCompetition>
          <IdStatus>6538</IdStatus>
          <Priority>
            <PriorityOther>264</PriorityOther>
          </Priority>
        </AddCompetitiveGroup>
      </AddCompetitiveGroupList>
    </Application>
    
    
    <Application>
      <IdObject>1438</IdObject>
      <EntrantChoice>
        <AddEntrant>
          <Identification>
            <IdDocumentType>1240</IdDocumentType>
            <DocName>string</DocName>
            <IssueDate>1985-10-19</IssueDate>
          </Identification>
          <IdGender>2580</IdGender>
          <Birthday>1978-05-12</Birthday>
          <Birthplace>string</Birthplace>
          <IdOksm>6570</IdOksm>
          <AddressList>
            <Address>
              <IsRegistration>1</IsRegistration>
              <FullAddr>string</FullAddr>
              <IdRegion>3931</IdRegion>
              <City>string</City>
            </Address>
          </AddressList>
        </AddEntrant>
      </EntrantChoice>
      <RegistrationDate>1972-10-05T10:59:00.98</RegistrationDate>
      <FirstHigherEducation>true</FirstHigherEducation>
      <NeedHostel>0</NeedHostel>
      <AllowedForEpgu>false</AllowedForEpgu>
      <IdStageAdmission>2427</IdStageAdmission>
      <IsBudget>1</IsBudget>
      <IdEducationLevelGroup>3502</IdEducationLevelGroup>
      <ExtraTestAttribute>0</ExtraTestAttribute>
      <AddCompetitiveGroupList>
        <AddCompetitiveGroup>
          <IdCompetition>3293</IdCompetition>
          <IdStatus>8653</IdStatus>
          <Priority>
            <PriorityTarget>86</PriorityTarget>
          </Priority>
        </AddCompetitiveGroup>
        <AddCompetitiveGroup>
          <IdCompetition>4365</IdCompetition>
          <IdStatus>2433</IdStatus>
          <Priority>
            <PriorityOther>66</PriorityOther>
          </Priority>
        </AddCompetitiveGroup>
        <AddCompetitiveGroup>
          <IdCompetition>6029</IdCompetition>
          <IdStatus>429</IdStatus>
          <Priority>
            <PriorityTarget>67</PriorityTarget>
          </Priority>
        </AddCompetitiveGroup>
        <AddCompetitiveGroup>
          <IdCompetition>3022</IdCompetition>
          <IdStatus>501</IdStatus>
          <Priority>
            <PriorityOther>36</PriorityOther>
          </Priority>
        </AddCompetitiveGroup>
        <AddCompetitiveGroup>
          <IdCompetition>2444</IdCompetition>
          <IdStatus>9256</IdStatus>
          <Priority>
            <PriorityTarget>203</PriorityTarget>
          </Priority>
        </AddCompetitiveGroup>
      </AddCompetitiveGroupList>
      <IdDictionaryValueMusic>457</IdDictionaryValueMusic>
    </Application>
    
  </ApplicationList>
</PackageData>



'''




'''

<?xml version="1.0" encoding="utf-8"?>
<!-- Created with Liquid Technologies Online Tools 1.0 (https://www.liquid-technologies.com) -->
<PackageData>
  <ApplicationList>
    <Application>
      <IdObject>4098</IdObject>
      <EntrantChoice>
        <AddEntrant>
          <Identification>
            <IdDocumentType>100001</IdDocumentType>  // паспорт DocumentTypeCls  вот тут возможно ошибка 
            <DocName>Паспорт гражданина Российской Федерации</DocName>  // выташил оттуда же 
            <DocSeries>8220</DocSeries>
            <DocNumber>665461</DocNumber>
            <DocOrganization>УФМС России</DocOrganization>
            <IssueDate>2011-11-02</IssueDate>
          </Identification>
          <IdGender>1</IdGender>
          <Birthday>2000-04-20</Birthday>
          <Birthplace>Mahachkala</Birthplace>
          <IdOksm>185</IdOksm>
          <AddressList>
            <Address>
              <IsRegistration>true</IsRegistration>
              <FullAddr>Mahachkala</FullAddr>
              <IdRegion>5</IdRegion>
              <City>izberg</City>
            </Address>
          </AddressList>
        </AddEntrant>
      </EntrantChoice>
      <RegistrationDate>1987-08-20T00:47:07.81</RegistrationDate>
      <FirstHigherEducation>true</FirstHigherEducation>
      <NeedHostel>true</NeedHostel>
      <AllowedForEpgu>true</AllowedForEpgu>
      <IdStageAdmission>1</IdStageAdmission> // основной набор / доп набор 4
      <IsBudget>true</IsBudget>
      <IdEducationLevelGroup>1</IdEducationLevelGroup>
      <ExtraTestAttribute>false</ExtraTestAttribute>
      <AddCompetitiveGroupList>
        <AddCompetitiveGroup>
          <IdCompetition>268943</IdCompetition>
          <IdStatus>1</IdStatus>
          <Priority>
            <PriorityTarget>112</PriorityTarget>
          </Priority>
        </AddCompetitiveGroup>
      </AddCompetitiveGroupList>
      <SpecialConditionList>
        <Id>2860</Id>
        <Id>1279</Id>
        <Id>6278</Id>
        <Id>2768</Id>
        <Id>9280</Id>
      </SpecialConditionList>
    </Application>
  </ApplicationList>
</PackageData>


'''





'''<FieldsDescription>{
    "fields":[
        {"type":"character","not_null":true,"xml_name":"SubdivisionCode","description":"Код организации"},
        {"type":"integer","not_null":true,"xml_name":"IdOksm","xml_cls":"OksmCls","description":"Страна выдачи"},
        {"type":"character","not_null":true,"xml_name":"Surname","description":"Фамилия"},
        {"type":"character","not_null":true,"xml_name":"Name","description":"Имя"},
        {"type":"character","not_null":false,"xml_name":"Patronymic","description":"Отчество"}
    ]}</FieldsDescription>
'''



'''
<?xml version="1.0" encoding="utf-8"?>
<!-- Created with Liquid Technologies Online Tools 1.0 (https://www.liquid-technologies.com) -->
<PackageData>
  <ApplicationList>
    <Application>
      <IdObject>4098</IdObject>
      <EntrantChoice>
        <AddEntrant>
          <Identification>
            <IdDocumentType>100001</IdDocumentType>
            <DocName>Паспорт гражданина Российской Федерации</DocName> 
            <DocSeries>8220</DocSeries>
            <DocNumber>665461</DocNumber>
            <DocOrganization>УФМС России</DocOrganization>
            <IssueDate>2011-11-02</IssueDate>
            <Fields>
              <SubdivisionCode>820-001</SubdivisionCode>
              <IdOksm>185</IdOksm>
              <Surname>Иванов</Surname>
              <Name>Иван</Name>
              <Patronymic>Иванович</Patronymic>
            </Fields>
          </Identification>
          <Snils>73286060298</Snils>
          <IdGender>1</IdGender>
          <Birthday>2000-04-20</Birthday>
          <Birthplace>Mahachkala</Birthplace>
          <IdOksm>185</IdOksm>
          <AddressList>
            <Address>
              <IsRegistration>true</IsRegistration>
              <FullAddr>Mahachkala</FullAddr>
              <IdRegion>5</IdRegion>
              <City>izberg</City>
            </Address>
          </AddressList>
        </AddEntrant>
      </EntrantChoice>
      <RegistrationDate>2025-06-12T15:44:19+03:00</RegistrationDate>
      <FirstHigherEducation>true</FirstHigherEducation>
      <NeedHostel>true</NeedHostel>
      <AllowedForEpgu>true</AllowedForEpgu>
      <IdStageAdmission>1</IdStageAdmission>
      <IsBudget>true</IsBudget>
      <IdEducationLevelGroup>1</IdEducationLevelGroup>
      <ExtraTestAttribute>false</ExtraTestAttribute>
      <AddCompetitiveGroupList>
        <AddCompetitiveGroup>
          <IdCompetition>268943</IdCompetition>
          <IdStatus>4</IdStatus>
          <Priority>
            <PriorityOther>1</PriorityOther>
          </Priority>
        </AddCompetitiveGroup>
      </AddCompetitiveGroupList>
    </Application>
  </ApplicationList>
</PackageData>


'''