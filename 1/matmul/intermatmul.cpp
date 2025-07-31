#include <CLI11/CLI11.hpp>
#include <fmt/ranges.h>
#include <fstream>
#include <iostream>
#include <tuple>
#include <vector>
#include <iomanip>
#include <chrono>

void matmul(const std::vector<double> &a, const std::vector<double> &b,
            std::vector<double> &d,
            std::tuple<unsigned, unsigned, unsigned> dims) {
  auto [m, n, k] = dims;
  for (int i = 0; i < m; i++) {
    for (int l = 0; l < k; l++) {
      for (int j = 0; j < n; j++) {
        d[i * n + j] += a[i * k + l] * b[l * n + j];
      }
    }
  }
}

int main(int argc, char *argv[]) {
  CLI::App app{"App description"};
  argv = app.ensure_utf8(argv);

  std::string filename = "";
  std::string output = "";
  app.add_option("input", filename, "");
  app.add_option("-o", output, "");

  CLI11_PARSE(app, argc, argv);

  if (filename == "")
    return 1;

  std::ifstream fin(filename);
  if (!fin.is_open())
    return 1;
  unsigned m, n, k;
  fin >> m >> n >> k;

  std::vector<double> a, b, d;
  a.reserve(m * k);
  b.reserve(k * n);
  d.resize(m * n);

  for (int i = 0; i < m; i++) {
    for (int j = 0; j < k; j++) {
      double t;
      fin >> t;
      a.push_back(t);
    }
  }

  for (int i = 0; i < k; i++) {
    for (int j = 0; j < n; j++) {
      double t;
      fin >> t;
      b.push_back(t);
    }
  }

  auto begin = std::chrono::steady_clock::now();
  matmul(a, b, d, {m, n, k});
  auto end = std::chrono::steady_clock::now();

  fmt::println("Time difference = {}s",
               std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin)
                   .count() / double(1000 * 1000 * 1000));

  if (output != "") {
    std::ofstream fout(output);
    fout << m << ' ' << n << '\n';
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        fout << std::fixed << std::setprecision(6) << d[i * n + j] << ' ';
      }
    }
    fout << '\n';
    return 0;
  }

  fmt::println("{}", d);
}