from sqlalchemy import Table, Column, ForeignKey

from database import Base


association_client_request_with_contractor_table = Table(
    'association_client_request_with_contractor',
    Base.metadata,
    Column('client_request_id', ForeignKey('citizen_requests.id'), \
            primary_key=True),
    Column('contractor_id', ForeignKey('contractors.id'), primary_key=True)
)

association_client_request_with_work_table = Table(
    'association_client_request_with_work',
    Base.metadata,
    Column('client_request_id', ForeignKey('citizen_requests.id'), \
            primary_key=True),
    Column('work_id', ForeignKey('works.id'), primary_key=True)
)

association_client_request_with_employee_table = Table(
    'association_client_request_with_employee',
    Base.metadata,
    Column('client_request_id', ForeignKey('citizen_requests.id'), \
            primary_key=True),
    Column('employee_id', ForeignKey('employees.id'), primary_key=True)
)

association_client_request_with_consultation_table = Table(
    'association_client_request_with_consultation',
    Base.metadata,
    Column('client_request_id', ForeignKey('citizen_requests.id'), \
            primary_key=True),
    Column('consultation_id', ForeignKey('consultations.id'), \
            primary_key=True)
)

association_contractor_with_house_table = Table(
    'association_contractor_with_house',
    Base.metadata,
    Column('contractor_id', ForeignKey('contractors.id'), primary_key=True),
    Column('house_id', ForeignKey('houses.id'), primary_key=True)
)

association_contractor_with_work_table = Table(
    'association_contractor_with_work',
    Base.metadata,
    Column('contractor_id', ForeignKey('contractors.id'), primary_key=True),
    Column('work_id', ForeignKey('works.id'), primary_key=True)
)

association_consultation_with_employee_table = Table(
    'association_consultation_with_employee',
    Base.metadata,
    Column('consultation_id', ForeignKey('consultations.id'), \
            primary_key=True),
    Column('employee_id', ForeignKey('employees.id'), primary_key=True)
)

association_meeting_with_client_table = Table(
    'association_meeting_with_client',
    Base.metadata,
    Column('meeting_id', ForeignKey('meetings.id'), primary_key=True),
    Column('citizen_id', ForeignKey('citizens.id'), primary_key=True)
)

association_request_document_with_work_table = Table(
    'association_request_document_with_work',
    Base.metadata,
    Column('request_document_id', ForeignKey('requests_documents.id'), \
            primary_key=True),
    Column('work_id', ForeignKey('works.id'), primary_key=True)
)

association_contract_with_work_table = Table(
    'association_contract_with_work',
    Base.metadata,
    Column('contract_id', ForeignKey('contracts.id'), primary_key=True),
    Column('work_id', ForeignKey('works.id'), primary_key=True)
)

