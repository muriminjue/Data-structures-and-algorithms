function binary_search(List, target) {
  let first = 0,
    last = List.length - 1;
  while (first <= last) {
    const midpoint = Math.floor((first + last) / 2);
    if (List[midpoint] === target) {
      return midpoint;
    } else if (List[midpoint] > target) {
      last = midpoint - 1;
    } else {
      first = midpoint + 1;
    }
  }
  return null;
}

function verify(index) {
  if (index) {
    console.log("Item found at index: ", index);
  } else {
    console.log("Item not found");
  }
}

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

let result = binary_search(numbers, 12);
verify(result);

result = binary_search(numbers, 6);
verify(result);
