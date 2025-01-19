class Profile:
    def __init__(self, name, age, gender, occupation, contact):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.contact = contact

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nOccupation: {self.occupation}\nContact: {self.contact}\n"


class Person:
    def __init__(self, profile, preferences=None):
        self.profile = profile
        self.preferences = preferences
        self.match = None

    def find_match(self, candidates):
        if self.profile is None or self.preferences is None:
            return False

        for candidate in candidates:
            if (
                candidate.profile
                and candidate.profile.age >= self.preferences['min_age']
                and candidate.profile.age <= self.preferences['max_age']
                and candidate.profile.gender == self.preferences['gender']
                and candidate.preferences['min_age'] <= self.profile.age
                and candidate.preferences['max_age'] >= self.profile.age
                and candidate.preferences['gender'] == self.profile.gender
            ):
                self.match = candidate
                candidate.match = self
                return True
        return False


class MarriageBureau:
    def __init__(self):
        self.people = []
        self.min_age_for_marriage_bureau = 18

    def create_person(self):
        name = input("Enter your full name: ")
        age = int(input("Enter your age: "))

        if age < self.min_age_for_marriage_bureau:
            print(
                f"Sorry, you are not of eligible age for the marriage bureau. The minimum age allowed is {self.min_age_for_marriage_bureau}."
            )
            return

        profile = Profile(
            name,
            age,
            input("Enter your gender (Male/Female/Other): "),
            input("Enter your occupation: "),
            input("Enter your contact number: "),
        )
        preferences = {
            'min_age': int(input("Enter your preferred minimum age: ")),
            'max_age': int(input("Enter your preferred maximum age: ")),
            'gender': input("Enter your preferred gender of the match: "),
        }
        person = Person(profile, preferences)
        self.people.append(person)
        print("\nProfile created successfully!\n")

    def display_all_profiles(self):
        if not self.people:
            print("No profiles found.")
        else:
            print("\n--- All Profiles ---")
            for person in self.people:
                print(person.profile)

    def search_matches(self):
        if len(self.people) < 2:
            print("Not enough profiles to find a match.")
            return

        name_to_find = input("Enter the name of the person to find a match for: ")
        person_to_find = None

        for person in self.people:
            if person.profile.name == name_to_find:
                person_to_find = person
                break

        if person_to_find is None:
            print(f"No person found with the name {name_to_find}.")
            return

        for candidate in self.people:
            if candidate != person_to_find:
                if person_to_find.find_match([candidate]):
                    print(f"{person_to_find.profile.name} is matched with {candidate.profile.name}")
                    break
        else:
            print(f"No match found for {person_to_find.profile.name}.")


def main():
    print("Welcome to the Marriage Bureau System")
    bureau = MarriageBureau()

    while True:
        print("\n1. Create profile\n2. Find matches\n3. Display all profiles\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bureau.create_person()
        elif choice == '2':
            if len(bureau.people) < 2:
                print("Not enough profiles to find a match. Create more profiles.")
            else:
                bureau.search_matches()
        elif choice == '3':
            bureau.display_all_profiles()
        elif choice == '4':
            print("Thanks for visiting the marriage bureau system. Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
