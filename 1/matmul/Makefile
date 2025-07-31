ifeq ($(DEBUG), 1)
	OPTFLAGS := -DDEBUG -O0 $(CFLAGS)
else
	OPTFLAGS := -O3 -DNDEBUG $(CFLAGS)
endif

DIMS := 128x128
VERIFIED_OUTPUT := ./data/$(DIMS)_output.txt
PYOUT := np_output.txt
NPOUT := np_output.txt
CPP_OUT := cpp_output.txt
CPP_INTER_OUT := cpp_inter_output.txt
CPP_TILED_OUT := cpp_tiled_output.txt

CXXFLAGS := -std=c++20
OPTLIB := -I ./third_party/CLI11/include/
FMTLIB := -DFMT_HEADER_ONLY=1 -I ./third_party/fmt/include/

FLAGS := $(OPTFLAGS) $(CXXFLAGS) $(OPTLIB) $(FMTLIB)

.PHONY = all runmatmul runall perfall perfmatmul perfintermatmul perftiledmatmul

all: matmul

matmul: matmul.cpp
	clang++ matmul.cpp $(FLAGS) -o matmul

runmatmul: matmul
	./matmul ./data/$(DIMS).txt -o $(CPP_INTER_OUT)

verifymatmul: $(CPP_OUT) $(VERIFIED_OUTPUT)
	python3 verify.py $(CPP_OUT) $(VERIFIED_OUTPUT)

perfmatmul: matmul
	sudo perf stat -e cache-references,cache-misses ./matmul ./data/$(DIMS).txt -o $(CPP_OUT)

intermatmul: intermatmul.cpp
	clang++ intermatmul.cpp $(FLAGS) -o intermatmul

runintermatmul: intermatmul
	./intermatmul ./data/$(DIMS).txt -o $(CPP_INTER_OUT)

verifyintermatmul: $(CPP_INTER_OUT) $(VERIFIED_OUTPUT)
	python3 verify.py $(CPP_INTER_OUT) $(VERIFIED_OUTPUT)

perfintermatmul: intermatmul
	sudo perf stat -e cache-references,cache-misses ./intermatmul ./data/$(DIMS).txt -o $(CPP_INTER_OUT)

tiledmatmul: tiledmatmul.cpp
	clang++ tiledmatmul.cpp $(FLAGS) -o tiledmatmul

runtiledmatmul: tiledmatmul
	./tiledmatmul ./data/$(DIMS).txt -o $(CPP_TILED_OUT)

verifytiledmatmul: $(CPP_TILED_OUT) $(VERIFIED_OUTPUT)
	python3 verify.py $(CPP_TILED_OUT) $(VERIFIED_OUTPUT)

perftiledmatmul: tiledmatmul
	sudo perf stat -e cache-references,cache-misses ./tiledmatmul ./data/$(DIMS).txt -o $(CPP_TILED_OUT)

runpy: matmul.py
	python3 matmul.py ./data/$(DIMS).txt -o $(PYOUT)

verifypy: $(PYOUT) $(VERIFIED_OUTPUT)
	python3 verify.py $(PYOUT) $(VERIFIED_OUTPUT)

runnp: npmatmul.py
	python3 npmatmul.py ./data/$(DIMS).txt -o $(NPOUT)

verifynppy: $(NPOUT) $(VERIFIED_OUTPUT)
	python3 verify.py $(NPOUT) $(VERIFIED_OUTPUT)

runall:
	python3 npmatmul.py ./data/$(DIMS).txt -o $(NPOUT)
	matmul ./data/$(DIMS).txt -o $(CPP_OUT)

perfall: perfmatmul perfintermatmul perftiledmatmul

clean:
	rm -rf matmul intermatmul tiledmatmul a.out
	rm -rf output.txt $(PYOUT) $(NPOUT) $(CPP_OUT) $(CPP_INTER_OUT) $(CPP_TILED_OUT)