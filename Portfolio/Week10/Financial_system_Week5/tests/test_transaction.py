from transaction import Transaction


def test_transaction_processing_and_description():
    record = Transaction("deposit", 30, "Deposit transaction")
    assert record.Status == "pending"
    record.process_transaction()
    record.set_description("Cash deposit")
    record.set_description("")
    assert str(record) == "deposit,30,Cash deposit,Processed"
    record.cancel_transaction()
    assert record.Status == "Cancelled"
