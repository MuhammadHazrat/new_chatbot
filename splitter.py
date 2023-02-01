import os

def join_pieces(filename, file_extension, start, end, outfile):
    with open(outfile, "wb") as outf:
        for i in range(start, end):
            chunk_filename = "{}_{}{}".format(filename, i, file_extension)
            with open(chunk_filename, "rb") as chunk_file:
                chunk = chunk_file.read()
                outf.write(chunk)
            os.remove(chunk_filename)

def join_first_two_pieces(filename, file_extension):
    join_pieces(filename, file_extension, 1, 3, "temp1.joblib")

def join_last_two_pieces(filename, file_extension):
    join_pieces(filename, file_extension, 3, 5, "temp2.joblib")

def join_big_pieces(filename, file_extension):
    with open("joblib_classifier.joblib", "wb") as outfile:
        with open("temp1.joblib", "rb") as chunk_file1:
            chunk = chunk_file1.read()
            outfile.write(chunk)
        os.remove("temp1.joblib")

        with open("temp2.joblib", "rb") as chunk_file2:
            chunk = chunk_file2.read()
            outfile.write(chunk)
        os.remove("temp2.joblib")

join_first_two_pieces("joblib_classifier", ".joblib")
join_last_two_pieces("joblib_classifier", ".joblib")
join_big_pieces("joblib_classifier", ".joblib")
