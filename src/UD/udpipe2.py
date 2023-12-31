import sys

from ufal.udpipe import Model, Pipeline, ProcessingError # pylint: disable=no-name-in-module

# In Python2, wrap sys.stdin and sys.stdout to work with unicode.
if sys.version_info[0] < 3:
    import codecs
    import locale
    encoding = locale.getpreferredencoding()
    sys.stdin = codecs.getreader(encoding)(sys.stdin)
    sys.stdout = codecs.getwriter(encoding)(sys.stdout)

if len(sys.argv) < 4:
    sys.stderr.write('Usage: %s input_format(tokenize|conllu|horizontal|vertical) output_format(conllu) model_file\n' % sys.argv[0])
    sys.exit(1)

sys.stderr.write('Loading model: ')
model = Model.load(sys.argv[3])
if not model:
    sys.stderr.write("Cannot load model from file '%s'\n" % sys.argv[3])
    sys.exit(1)
sys.stderr.write('done\n')

pipeline = Pipeline(model, sys.argv[1], Pipeline.DEFAULT, Pipeline.DEFAULT, sys.argv[2])
error = ProcessingError()

# Read whole input
text = open(sys.argv[4], "r")
fout = open(sys.argv[5], "a")
app_file, i = "", 0

for line in text:
    if i == 1000:
        # Process data
        processed = pipeline.process(app_file, error)
        if error.occurred():
            sys.stderr.write("An error occurred when running run_udpipe: ")
            sys.stderr.write(error.message)
            sys.stderr.write("\n")
            sys.exit(1)
        fout.write(processed)
        app_file, i = "", 0
    else:
        app_file += line
        i += 1

if i != 0:
    # Process data
    processed = pipeline.process(app_file, error)
    if error.occurred():
        sys.stderr.write("An error occurred when running run_udpipe: ")
        sys.stderr.write(error.message)
        sys.stderr.write("\n")
        sys.exit(1)
    fout.write(processed)
    app_file, i = "", 0