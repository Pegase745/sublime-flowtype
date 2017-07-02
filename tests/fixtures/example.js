// @flow

// A type describing a person
type Person = {
	firstName: string,
	lastName: string,
};

// A function returning a full name
function fullName(firstName: string, lastName) {
	return `${firstName} ${lastName}`;
}

const user: Person = {
	firstName: 'Lorem',
	lastName: 'Ipsum',
};
