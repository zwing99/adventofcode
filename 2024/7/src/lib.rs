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

#[pyfunction]
fn bfs_rust(total: u128, target: u128, nums: Vec<u128>) -> PyResult<u128> {
    let mut visited = Vec::new();
    let mut queue = Vec::new();
    let mut node_index = 0;
    let start = nums[node_index];
    queue.push((start, node_index));
    visited.push((start, node_index));
    let mut found = false;
    //println!("target: {}", target);
    while let Some((v, i)) = queue.pop() {
        let next_i = i + 1;
        if next_i >= nums.len() {
            continue;
        }
        let n = nums[next_i];
        for op in &[mul, add, concat] {
            let next_v = op(v, n);
            if next_i + 1 == nums.len() && next_v == target {
                //println!("({}, {})", next_v, next_i);
                found = true;
                break;
            }
            if !visited.contains(&(next_v, next_i)) && next_i + 1 < nums.len() && next_v <= target {
                //println!("({}, {})", next_v, next_i);
                visited.push((next_v, next_i));
                queue.push((next_v, next_i));
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
    Ok(())
}
