import hashlib
import time
from record import HealthRecord

class Block:
    def __init__(self, index, timestamp, record, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.record = record
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.record}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return f"Block #{self.index}\nTimestamp: {self.timestamp}\n{self.record}\nHash: {self.hash}\nPrevious Hash: {self.previous_hash}\n"


class Blockchain:
    def __init__(self):
        # Initialize the blockchain with the genesis block
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Create the first (genesis) block of the blockchain with a dummy record
        return Block(0, time.time(), HealthRecord("0", "Genesis", 0, "None", "None"), "0")

    def get_last_block(self):
        # Retrieve the last (most recent) block in the chain
        return self.chain[-1]

    def add_block(self, record):
        # Add a new block containing a health record to the blockchain
        last_block = self.get_last_block()
        new_block = Block(len(self.chain), time.time(), record, last_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Check the validity of the blockchain by verifying hash integrity
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.compute_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def print_chain(self):
        # Print the full blockchain
        for block in self.chain:
            print(block)

    def get_record_by_id(self, patient_id):
        # Retrieve a health record by the patient ID
        for block in self.chain:
            if block.record.patient_id == patient_id:
                return block.record
        return None
