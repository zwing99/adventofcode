use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: i64, b: i64) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyclass(eq, eq_int)]
#[derive(PartialEq, Clone)]
enum Part {
    Part1 = 1,
    Part2 = 2,
}

/// A Python module implemented in Rust.
#[pymodule]
fn aoc2024_7(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_class::<Part>()?;
    Ok(())
}
