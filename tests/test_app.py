from streamlit.testing.v1 import AppTest
from io import StringIO
import pandas as pd


def test_app():
    """Test the Streamlit app functionality."""
    # Mock CSV data
    mock_csv_data = "col1,col2,col3\n1,2,3\n4,5,6\n7,8,9"
    mock_file = StringIO(mock_csv_data)
    mock_file.name = "mock_data.csv"

    test = AppTest.from_file("streamlit_1.py").run()

    assert test.success

    assert "Data Preview" in test.stdout
    assert "Summary Statistics" in test.stdout

    # Mock reading and comparing the DataFrame
    expected_df = pd.read_csv(StringIO(mock_csv_data))
    # This assumes that the app assigns the DataFrame to session state or outputs it visibly
    # Validate that the app processed the data correctly
    assert str(expected_df.describe()) in test.stdout
