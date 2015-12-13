# solve.py

from board import Board
from stack import Stack, MinPQ

class Solver(object):

	class _Node(object):

		def __init__(self, board, moves = 0, prev = None):
			self.board = board
			self.moves = moves
			self.prev  = prev

		def priority(self):
			return self.board.manhattan() + self.moves

		def __cmp__(self, other):
			return self.priority() - other.priority()

	def __init__(self, board):
		self.pq = MinPQ()
		self.goal = None

		self.pq.insert(self._Node(board))

		while True:
			node = self.pq.delMin()

			if node.board.goal():
				self.goal = node
				break
			for neighbor in node.board.neighbors():
				n = self._Node(neighbor, node.moves + 1, node)
				if not node.prev is None:
					if neighbor != node.board:
						self.pq.insert(n)
				else:
					self.pq.insert(n)

	def moves(self):
		return self.goal.moves if not self.goal is None else -1

	def solution(self):
		stck = Stack()
		node = self.goal
		while not node is None:
			stck.push(node.board)
			node = node.prev
		return stck

if __name__ == '__main__':

	#blocks  = [[0,1,3],[4,2,5],[7,8,6]]
	#blocks = [[6,0,5],[8,7,4],[3,2,1]]
	#blocks = [[8,6,7],[2,5,4],[1,3,0]]
	#blocks = [[2,3,4,8],[1,6,0,12],[5,10,7,11],[9,13,14,15]]
	#blocks = [[5,1,8],[2,7,3],[4,0,6]]
	blocks = [[1,2,3,4],[6,10,7,8],[5,0,11,12],[9,13,14,15]]
	initial = Board(blocks)

	# check if puzzle is solvable; if so, solve it and output solution
	if initial.isSolvable():
		solver = Solver(initial)
		print "Minimum number of moves = %r" % solver.moves()
		for board in solver.solution():
			print board
	else:
		print "Unsolvable"