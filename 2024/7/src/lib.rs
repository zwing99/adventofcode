use std::collections::{HashSet, VecDeque};

use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

fn mul(a: u128, b: u128) -> u128 {
    a * b
}

fn add(a: u128, b: u128) -> u128 {
    a + b
}

fn concat(a: u128, b: u128) -> u128 {
    format!("{}{}", a, b).parse::<u128>().unwrap()
}

#[pyclass(eq, eq_int)]
#[derive(PartialEq, Clone)]
enum Part {
    Part1 = 1,
    Part2 = 2,
}

#[pyfunction]
fn bfs_rust(total: u128, target: u128, nums: Vec<u128>, part: Part) -> PyResult<u128> {
    let mut visited = HashSet::<(u128, usize)>::new();
    let mut queue = VecDeque::<(u128, usize)>::new();
    let node_index: usize = 0;
    let start = nums[node_index];
    queue.push_front((start, node_index));
    visited.insert((start, node_index));
    let mut found = false;
    let len_nums = nums.len();
    //println!("target: {}", target);
    let p1funcs = vec![mul, add];
    let p2funcs = vec![mul, add, concat];
    let funcs = match part {
        Part::Part1 => &p1funcs,
        Part::Part2 => &p2funcs,
    };
    while let Some((v, i)) = queue.pop_front() {
        let next_i = i + 1;
        if next_i >= len_nums {
            continue;
        }
        let n = nums[next_i];
        for op in funcs.iter() {
            let next_v = op(v, n);
            if next_i + 1 == len_nums && next_v == target {
                //println!("({}, {})", next_v, next_i);
                found = true;
                break;
            }
            if !visited.contains(&(next_v, next_i)) && next_i + 1 < len_nums && next_v <= target {
                //println!("({}, {})", next_v, next_i);
                visited.insert((next_v, next_i));
                queue.push_back((next_v, next_i));
            }
        }
        if found {
            break;
        }
    }

    if found {
        //println!("found");
        Ok(total + target)
    } else {
        Ok(total)
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn aoc2024_7(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(bfs_rust, m)?)?;
    m.add_class::<Part>()?;
    Ok(())
}
