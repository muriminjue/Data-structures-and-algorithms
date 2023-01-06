function linear_search(List, target) {
  /*
    Loop through list and return index of target if found and none if note null
    */
  for (const [index, item] of List.entries()) {
    if (item == target) return index;
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

let result = linear_search(numbers, 12);
verify(result);

result = linear_search(numbers, 6);
verify(result);
