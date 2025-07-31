CC := g++
ifeq ($(DEBUG), 1)
	OPTFLAGS := -DDEBUG -O0 $(CFLAGS)
else
	OPTFLAGS := -O3 -DNDEBUG $(CFLAGS)
endif

DIMS := 128x128
INPUT := ./data/$(DIMS).txt
VERIFIED_OUTPUT := ./data/$(DIMS)_output.txt
PYOUT := np_output.txt
NPOUT := np_output.txt
CPP_OUT := cpp_output.txt
CPP_INTER_OUT := cpp_inter_output.txt
CPP_TILED_OUT := cpp_tiled_output.txt
CPP_OMP_OUT := cpp_omp_output.txt

CXXFLAGS := -std=c++20
OPTLIB := -I ./third_party/CLI11/include/
FMTLIB := -DFMT_HEADER_ONLY=1 -I ./third_party/fmt/include/

FLAGS := $(OPTFLAGS) $(CXXFLAGS) $(OPTLIB) $(FMTLIB)

.PHONY = all runmatmul runall perfall perfmatmul perfintermatmul perftiledmatmul

all: matmul

gen_output: npmatmul.py
	python3 npmatmul.py $(INPUT) -o $(VERIFIED_OUTPUT)

matmul: matmul.cpp
	$(CC) matmul.cpp $(FLAGS) -o matmul

runmatmul: matmul
	./matmul $(INPUT) -o $(CPP_INTER_OUT)

verifymatmul: $(CPP_OUT) $(VERIFIED_OUTPUT)
	python3 verify.py $(CPP_OUT) $(VERIFIED_OUTPUT)

perfmatmul: matmul
	sudo perf stat -e cache-references,cache-misses ./matmul $(INPUT) -o $(CPP_OUT)

intermatmul: intermatmul.cpp
	$(CC) intermatmul.cpp $(FLAGS) -o intermatmul

runintermatmul: intermatmul
	./intermatmul $(INPUT) -o $(CPP_INTER_OUT)

verifyintermatmul: $(CPP_INTER_OUT) $(VERIFIED_OUTPUT)
	python3 verify.py $(CPP_INTER_OUT) $(VERIFIED_OUTPUT)

perfintermatmul: intermatmul
	sudo perf stat -e cache-references,cache-misses ./intermatmul $(INPUT) -o $(CPP_INTER_OUT)

tiledmatmul: tiledmatmul.cpp
	$(CC) tiledmatmul.cpp $(FLAGS) -o tiledmatmul

runtiledmatmul: tiledmatmul
	./tiledmatmul $(INPUT) -o $(CPP_TILED_OUT)

verifytiledmatmul: $(CPP_TILED_OUT) $(VERIFIED_OUTPUT)
	python3 verify.py $(CPP_TILED_OUT) $(VERIFIED_OUTPUT)

perftiledmatmul: tiledmatmul
	sudo perf stat -e cache-references,cache-misses ./tiledmatmul $(INPUT) -o $(CPP_TILED_OUT)

ompmatmul: ompmatmul.cpp
	$(CC) -fopenmp ompmatmul.cpp $(FLAGS) -o ompmatmul

runompmatmul: ompmatmul
	./ompmatmul $(INPUT) -o $(CPP_OMP_OUT)

verifyompmatmul: $(CPP_OMP_OUT) $(VERIFIED_OUTPUT)
	python3 verify.py $(CPP_OMP_OUT) $(VERIFIED_OUTPUT)

runpy: matmul.py
	python3 matmul.py $(INPUT) -o $(PYOUT)

verifypy: $(PYOUT) $(VERIFIED_OUTPUT)
	python3 verify.py $(PYOUT) $(VERIFIED_OUTPUT)

runnp: npmatmul.py
	python3 npmatmul.py $(INPUT) -o $(NPOUT)

verifynppy: $(NPOUT) $(VERIFIED_OUTPUT)
	python3 verify.py $(NPOUT) $(VERIFIED_OUTPUT)

runall:
	python3 npmatmul.py $(INPUT) -o $(NPOUT)
	matmul $(INPUT) -o $(CPP_OUT)

perfall: perfmatmul perfintermatmul perftiledmatmul

clean:
	rm -rf matmul intermatmul tiledmatmul ompmatmul a.out
	rm -rf output.txt $(PYOUT) $(NPOUT) $(CPP_OUT) $(CPP_INTER_OUT) $(CPP_TILED_OUT) $(CPP_OMP_OUT)