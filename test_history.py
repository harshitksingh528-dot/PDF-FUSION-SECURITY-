from history_manager import HistoryManager


history = HistoryManager("test_history.json")

history.clear_history()

record = history.add_record(
    operation="Merge and Protect",
    pdf_count=2,
    total_pages=12,
    output_file="final_test.pdf",
    protected=True
)

print("New record:")
print(record)

print()

print("Total operations:")
print(history.get_operation_count())

print()

print("All history:")
print(history.get_history())