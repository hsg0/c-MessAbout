SONGS = [
	"Dancing Queen",
	"Country Roads",
	"Bohemian Rhapsody",
	"Hotel California",
	"Imagine",
	"Hey Jude",
	"Smells Like Teen Spirit",
	"Billie Jean",
	"Like a Rolling Stone",
	"I Will Always Love You",
	"Thriller",
	"Rolling in the Deep",
	"Lose Yourself",
	"Sweet Child O' Mine",
	"Shake It Off",
	"Uptown Funk",
	"Shape of You",
	"Blinding Lights",
	"Hallelujah",
	"Stairway to Heaven",
]

# start with an empty queue; users add entries via the menu
queue = []


def show_queue(queue):
	"""print everyone currently in the queue"""
	print()
	print("Current queue:")
	print()
	if not queue:
		print("(empty)")
	else:
		for singer in queue:
			name, song = singer
			print(f"{name} - {song}")
	print()
	print("Options: add / remove / quit")


def prompt_for_singer():
	name = input("Name: ").strip()

	# show songs and let user pick by number
	print()
	print("Select a song from the list (or 0 to enter a custom song):")
	for i, s in enumerate(SONGS, start=1):
		print(f"{i}. {s}")

	while True:
		choice = input("Song number (0 for custom): ").strip()
		if not choice.isdigit():
			print("Please enter a number.")
			continue
		idx = int(choice)
		if idx == 0:
			song = input("Enter song title: ").strip()
			break
		if 1 <= idx <= len(SONGS):
			song = SONGS[idx - 1]
			break
		print(f"Choose a number between 0 and {len(SONGS)}.")

	return name, song


def add_singer(queue):
	"""Ask for the singer and add them to the queue"""
	name, song = prompt_for_singer()
	if name and song:
		queue.append((name, song))
		print(f"Added {name} - {song}")
	else:
		print("Both name and song are required.")


def remove_singer(queue):
	"""Remove singer from the queue"""
	if queue:
		removed = queue.pop(0)
		print(f"Removed {removed[0]} - {removed[1]}")
	else:
		print("Queue is empty.")


def run_app(queue):
	print("=" * 44)
	print("Welcome to Sing Out: A Karaoke Queue Manager")
	print("=" * 44)

	is_running = True

	while is_running:
		show_queue(queue)
		selection = input("> ").strip().lower()

		if selection == "add":
			add_singer(queue)
		elif selection == "remove":
			remove_singer(queue)
		elif selection == "quit":
			is_running = False
		else:
			print("Unknown option. Please choose add/remove/quit.")


if __name__ == "__main__":
	run_app(queue)





