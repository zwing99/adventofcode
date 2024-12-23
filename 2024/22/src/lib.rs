use std::collections::{HashMap, HashSet};

use pyo3::prelude::*;

const PRUNE: i64 = 16777216;
type TupleOfFour = (i64, i64, i64, i64);

fn sum(tuple: &TupleOfFour) -> i64 {
    tuple.0 + tuple.1 + tuple.2 + tuple.3
}

#[pyfunction]
fn do_it(values: Vec<i64>) -> PyResult<i64> {
    let mut a: Vec<Vec<i64>> = Vec::with_capacity(values.len());
    for v in &values {
        let mut sn: i64 = *v;
        let mut seq: Vec<i64> = Vec::with_capacity(2000);
        for _ in 0..2000 {
            sn = ((sn * 64) ^ sn) % PRUNE;
            sn = ((sn / 32) ^ sn) % PRUNE;
            sn = ((sn * 2048) ^ sn) % PRUNE;
            seq.push(sn % 10);
        }
        a.push(seq);
    }

    let mut patterns: HashSet<TupleOfFour> = HashSet::new();
    let mut b: Vec<HashMap<TupleOfFour, i64>> = Vec::with_capacity(values.len());
    for v in a {
        let mut b_map: HashMap<TupleOfFour, i64> = HashMap::new();
        for i in 0..(v.len() - 4) {
            let new_pattern: TupleOfFour = (
                v[i + 1] - v[i],
                v[i + 2] - v[i + 1],
                v[i + 3] - v[i + 2],
                v[i + 4] - v[i + 3],
            );
            if sum(&new_pattern) >= 0 {
                patterns.insert(new_pattern);
                if !b_map.contains_key(&new_pattern) {
                    b_map.insert(new_pattern, v[i + 4]);
                }
            }
        }
        b.push(b_map);
    }

    let mut best: i64 = 0;
    for p in patterns {
        let mut total = 0;
        for v in &b {
            if v.contains_key(&p) {
                total += v[&p];
            }
        }
        if total > best {
            best = total;
        }
    }

    return Ok(best);
}

/// A Python module implemented in Rust.
#[pymodule]
fn aoc_2024_22(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(do_it, m)?)?;
    Ok(())
}
